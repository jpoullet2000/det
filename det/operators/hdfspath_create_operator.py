from hdfs import InsecureClient, HdfsError
import logging

from det.task import BaseOperator
from det.exceptions import DETException
from det import app

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
    Create an HDFS folder and record the dataset on Atlas

    Args:
      
    Returns:
      
    """
    def __init__(self, proxy_user=None):
        self.proxy_user = proxy_user
    
    def get_conn(self):
        try:
            nn = get_hdfs_namenode()
            logging.debug('Trying namenode {}'.format(nn.host))
            # TO BE IMPLEMENTED
            return client
        except HdfsError as e:
            logging.debug("Read operation on namenode {nn.host} failed with"
                          " error: {e.message}".format(**locals()))
     

