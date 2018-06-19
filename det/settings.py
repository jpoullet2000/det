import os
import socket

if 'DET_HOME' not in os.environ:
    os.environ['DET_HOME'] = os.path.join(os.path.expanduser('~'), '.det')

if not os.path.exists(os.environ['DET_HOME']):
    os.makedirs(os.environ['DET_HOME'])

# DEFAULT
DEFAULT_CLUSTER = 'localhost'

# DET
DET_WEBSERVER_PORT = 8888
DET_WEBSERVER_PORT_DEV = 8889
DET_WEBSERVER_ADDRESS = 'localhost' #'{}'.format(socket.gethostname())
DET_WEBSERVER_TIMEOUT = 45
DET_WORKERS = 2

# HDFS
HDFS_USER = 'hdfs'  # impersonation as HDFS_USER when creating hdfs folder, if not use None
HDFS_DATA_ROOT_FOLDER = '/data'
HDFS_CODE_ROOT_FOLDER = '/code'
HDFS_DATA_INGESTION_FOLDER_STRUCTURE = '/data/{{ env }}/raw/{{ app }}'
HDFS_DATA_DELIVERY_FOLDER_STRUCTURE = '/data/{{ env }}/{{ app }}/out'

# ATLAS
ATLAS_SERVER = 'localhost'
ATLAS_PORT = 21000

# AMBARI
AMBARI_SERVER = 'localhost'
AMBARI_PORT = 8080

# WEBHDFS
WEBHDFS_HOST = 'localhost'
WEBHDFS_PORT = 50070

# SECURITY
KERBEROS_ACTIVE = False

# TEST CREDENTIALS
TEST_ATLAS_LOGIN = 'atlas_login'
TEST_ATLAS_PASSWORD = 'atlas_password'
TEST_AMBARI_LOGIN = 'ambari_login'
TEST_AMBARI_PASSWORD = 'ambari_password'
TEST_DET_API_TOKEN = 'mytoken'
