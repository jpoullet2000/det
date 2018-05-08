import logging
from jinja2 import Template
from hdfs import InsecureClient, HdfsError

from det.task import BaseOperator
from det.exceptions import DETException
from det.operators.atlas_entity_create import AtlasEntityCreateOperator
from det.app import HDFS_CLIENT
from det.app import APP

_HDFS_USER = APP.app.config['HDFS_USER']
_HDFS_DATA_ROOT_FOLDER = APP.app.config['HDFS_DATA_ROOT_FOLDER']
_HDFS_DATA_CODE_FOLDER = APP.app.config['HDFS_CODE_ROOT_FOLDER']
_HDFS_DATA_INGESTION_FOLDER_STRUCTURE = APP.app.config['HDFS_DATA_INGESTION_FOLDER_STRUCTURE']
_HDFS_DATA_DELIVERY_FOLDER_STRUCTURE = APP.app.config['HDFS_DATA_DELIVERY_FOLDER_STRUCTURE']
_KERBEROS_ACTIVE = APP.app.config['KERBEROS_ACTIVE']
_DEFAULT_CLUSTER = APP.app.config['DEFAULT_CLUSTER']

if _KERBEROS_ACTIVE:
    try:
        from hdfs.ext.kerberos import KerberosClient
    except ImportError:
        logging.error('Could not load the Kerberos extension for the HDFSPathCreateOperator.')
        raise


class HDFSPathCreateOperatorException(DETException):
    pass


class HdfsPathCreateOperator(BaseOperator):
    """
    Creates an HDFS folder and records the dataset on Atlas
    """
    def __init__(self, hdfs_path_item, proxy_user=None):
        """
        Args:
            hdfs_path_item(HdfsPathItem): 
      
        Returns:
      
        """
        self.proxy_user = proxy_user
        self.hdfs_path_item = hdfs_path_item
        super(HdfsPathCreateOperator, self).__init__()

    @property
    def hdfs_path(self):
        if self.hdfs_path_item.data_code == 'code':
            raise HDFSPathCreateOperatorException('Code folder is not yet implemented')
        if self.hdfs_path_item.delivery_ingestion == 'delivery':
            logging.info('Building delivery path')
            folder_structure = Template(_HDFS_DATA_DELIVERY_FOLDER_STRUCTURE)
        else:
            logging.info('Building ingestion path')
            folder_structure = Template(_HDFS_DATA_INGESTION_FOLDER_STRUCTURE)
        if self.hdfs_path_item.subfolder:
            return '{}/{}'.format(
                folder_structure.render(env=self.hdfs_path_item.env,
                                        app=self.hdfs_path_item.app),
                self.hdfs_path_item.subfolder)
        return folder_structure.render(env=self.hdfs_path_item.env,
                                       app=self.hdfs_path_item.app)

    def get_conn(self):
        try:
            connection_str = HDFS_CLIENT.webhdfs_uri
            logging.debug('Trying uri %s', connection_str)
            if _KERBEROS_ACTIVE:
                client = KerberosClient(connection_str)
            else:
                proxy_user = self.proxy_user
                client = InsecureClient(connection_str, user=proxy_user)
            client.status('/')
            logging.debug('Using HDFS uri %s for hook', connection_str)
            return client
        except HdfsError as err:
            logging.debug('Read operation from uri {connection_str} failed with'
                          ' error: {err}'.format(**locals()))

    def create_hdfs_folder(self, current_hdfs_client):
        try:
            current_hdfs_client.makedirs(hdfs_path=self.hdfs_path)
        except:
            raise HDFSPathCreateOperatorException('HDFS folder could not be created')

    def delete_hdfs_folder(self, current_hdfs_client, recursive=True):
        """Delete HDFS folder if exists
        """
        try:
            current_hdfs_client.delete(self.hdfs_path, recursive)
        except:
            raise HDFSPathCreateOperatorException('HDFS folder {} could not be deleted'
                                                  .format(self.hdfs_path))

    def get_cluster_name(self):
        """ Get cluster name (where the hdfs path will be handled)

        Cluster name is the one provided via the API, if none is provided it uses DEFAULT_CLUSTER

        TO BE DONE:
        if none is provided it depends on the CLUSTER_SELECT_MODE:
        if CLUSTER_SELECT_MODE == 'env' : CLUSTER is chosen depending on the env ('dev', 'tst', 'acc', 'prod')
        if CLUSTER_SELECT_MODE == 'local':  CLUSTER is chosen as DEFAULT_CLUSTER
        """
        if hasattr(self.hdfs_path_item, 'cluster_name'):
            return self.hdfs_path_item.cluster_name
        return _DEFAULT_CLUSTER

#    def build_classification_list(self, keys=None):
#        keys = keys or ['cl', 'sg', 'fb', 'retainable']
#        classifications = list()
#        for key in keys:
#            classification_typename = getattr(self.hdfs_path_item.classification, key) 
#            classification = {'typeName': classification_typeName}
#            if key == 'retainable':
#                classfication['retentionPeriod'] = 365

    def create_atlas_hdfs_path(self, current_hdfs_client):
        """
        """
        try:
            attributes_=dict(qualifiedName=self.hdfs_path,
                             name=self.hdfs_path.replace('/', '_')[1:],
                             path=self.hdfs_path,
                             clusterName=self.get_cluster_name())
            entity_create_op = AtlasEntityCreateOperator(
                attributes = {k: v for k, v in attributes_.items() if v is not None},
                classifications=[getattr(self.hdfs_path_item.classification, a) for a in ['cl', 'sg', 'fb']],
                entity_type='hdfs_path')
            entity_create_op.execute()

        except:
            self.delete_hdfs_folder(current_hdfs_client)
            raise HDFSPathCreateOperatorException('Atlas hdfs path could not be created.'
                                                  'The HDFS folder has therefore been deleted.')

    def execute(self, context=None):
        current_hdfs_client = self.get_conn()
        self.create_hdfs_folder(current_hdfs_client)
        self.create_atlas_hdfs_path(current_hdfs_client)
