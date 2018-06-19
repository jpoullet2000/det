import logging
from jinja2 import Template
from hdfs import InsecureClient, HdfsError

from det.task import BaseOperator
from det.exceptions import DETException
from det.operators.atlas_entity_create import AtlasEntityCreateOperator
from det.app import HDFS_CLIENT
from det.app import APP
from det.utils.tools import get_env_type

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
    def __init__(self, hdfs_path_item, proxy_user=_HDFS_USER):
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
                client = KerberosClient(connection_str, proxy=self.proxy_user)
            else:
                client = InsecureClient(connection_str, user=self.proxy_user)
            client.status('/')
            logging.debug('Using HDFS uri %s for hook', connection_str)
            return client
        except HdfsError as err:
            logging.debug('Read operation from uri {connection_str} failed with'
                          ' error: {err}'.format(**locals()))

    def create_hdfs_folder(self, current_hdfs_client):
        try:
            #import pdb; pdb.set_trace()
            mypath = self.hdfs_path.lower()
            logging.info('The folder {} has been created'.format(mypath))
            current_hdfs_client.makedirs(hdfs_path=mypath)
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


    def build_environment_classification(self):
        env = self.hdfs_path_item.env
        app = self.hdfs_path_item.app
        env_type = get_env_type(env)
        env_class = "EN_{app}_{env_type}".format(**locals())
        return env_class

    def build_classification_list(self, keys=None):
        """ Build the classification dictionary that will be posted to Atlas

        TODO: this function is very specific (the required fields are hardcoded: cl, sg, ...)
              For better maintenance and evolution it should be based on the swagger file
        """
        keys = keys or ['Retainable', 'cl', 'sg', 'pl']
        classifications = list()
        for key in keys:
            if key == 'Retainable':
                classification_typename = key
            else:
                classification_typename = getattr(self.hdfs_path_item.classification, key)
            classification = {'typeName': classification_typename}
            if key == 'Retainable':
                classification['attributes'] = {'retentionPeriod': self.hdfs_path_item.classification.retainable.retention_period}
            classifications.append(classification)
        classifications.append({'typeName': self.build_environment_classification()})
        return classifications

    def create_atlas_hdfs_path(self, current_hdfs_client):
        """
        """
        try:
            hdfs_path = self.hdfs_path.lower()
            attributes_=dict(qualifiedName=hdfs_path,
                             name=hdfs_path.replace('/', '_')[1:],
                             path=hdfs_path,
                             clusterName=self.get_cluster_name())
            entity_create_op = AtlasEntityCreateOperator(
                attributes = {k: v for k, v in attributes_.items() if v is not None},
                classifications=self.build_classification_list(),
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
