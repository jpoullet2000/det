from hdfs import InsecureClient, HdfsError
import logging
from jinja2 import Template

from det.task import BaseOperator
from det.exceptions import DETException
from det.cli import app, atlas_client
from det.cli import hdfs
from det.operators.atlas_entity_create import AtlasEntityCreateOperator
# from det.utils.ambari import Ambari

_hdfs_user = app.app.config['HDFS_USER']
_hdfs_data_root_folder = app.app.config['HDFS_DATA_ROOT_FOLDER']
_hdfs_data_code_folder = app.app.config['HDFS_CODE_ROOT_FOLDER']
_hdfs_data_ingestion_folder_structure = app.app.config['HDFS_DATA_INGESTION_FOLDER_STRUCTURE']
_hdfs_data_delivery_folder_structure = app.app.config['HDFS_DATA_DELIVERY_FOLDER_STRUCTURE']
_kerberos_active = app.app.config['KERBEROS_ACTIVE']  

if _kerberos_active:
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
   
    @property
    def hdfs_path(self):
        if self.hdfs_path.item.data_code == 'code':
            raise HDFSPathCreateOperatorException('Code folder is not yet implemented')
        if self.hdfs_path_item.delivery_ingestion == 'delivery':
            logging.info('Building delivery path')
            folder_structure = Template(_hdfs_data_delivery_folder_structure)
            if hdfs_path_item.app_subfolders:
                return '{}/{}'.format(
                                      folder_structure.render(env=hdfs_path_item.env,
                                                              app=hdfs_path_item.app),
                                      hdfs_path_item.app_subfolders)
            else:
                return folder_structure.render(env=hdfs_path_item.env,
                                               app=hdfs_path_item.app)
        else:
            logging.info('Building ingestion path')
            folder_structure = Template(_hdfs_data_ingestion_folder_structure)
            if hdfs_path_item.src_subfolders:
                return '{}/{}'.format(
                                      folder_structure.render(env=hdfs_path_item.env,
                                                              src=hdfs_path_item.src),
                                      hdfs_path_item.src_subfolders)
            else:
                return folder_structure.render(env=hdfs_path_item.env,
                                               src=hdfs_path_item.src)

    def get_conn(self):
        try:
            connection_str = hdfs.get_uri()
            logging.debug('Trying uri {}'.format(hdfs_uri))
            if _kerberos_security_mode:
                client = KerberosClient(connection_str)
            else:
                proxy_user = self.proxy_user
                client = InsecureClient(connection_str, user=proxy_user)
            client.status('/')
            self.log.debug('Using HDFS uri %s for hook', hdfs_uri)
            return client
        except HdfsError as e:
            logging.debug("Read operation from uri {hdfs_uri} failed with"
                          " error: {e.message}".format(**locals()))

    def create_hdfs_folder(self, hdfs_client):
        try: 
            hdfs_client.makedirs(hdfs_path=self.hdfs_path)    
        except: 
            raise HDFSPathCreateOperatorException('HDFS folder could not be created')

    def delete_hdfs_folder(self, hdfs_client, recursive=False):
        """Delete HDFS folder if exists
        """
        hdfs_client.delete(self.hdfs_path, recursive)

    def create_atlas_hdfs_path(self):
        """
        """
        try:
            entity_create_op = AtlasEntityCreateOperator(attributes=dict(qualified_name = self.hdfs_path,
                                                                         name = self.hdfs_path.replace('/','_'),
                                                                         path = self.hdfs_path),
                                                         classifications=self.hdfs_path_item.classifications,
                                                         entity_type='hdfs_path')
            entity_create_op.execute()

        except:
            self.delete_hdfs_folder(hdfs_client)
            raise HDFSPathCreateOperatorException('Atlas hdfs path could not be created.'
                                                  'The HDFS folder has therefore been deleted.')

    def execute(self, context):
        hdfs_client = self.get_conn()
        self.create_hdfs_folder(hfds_client)
        self.create_atlas_hdfs_path(hdfs_client)
