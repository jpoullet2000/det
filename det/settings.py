import os
import socket

if 'DET_HOME' not in os.environ:
    os.environ['DET_HOME'] = os.path.join(os.path.expanduser('~'), '.det')

if not os.path.exists(os.environ['DET_HOME']):
    os.makedirs(os.environ['DET_HOME'])

# DEFAULT
DEFAULT_CLUSTER = 'el1538'

# DET
DET_WEBSERVER_PORT = 8888
DET_WEBSERVER_PORT_DEV = 8889
DET_WEBSERVER_ADDRESS = 'localhost' #'{}'.format(socket.gethostname())
DET_WEBSERVER_TIMEOUT = 45
DET_WORKERS = 2

# HDFS
HDFS_USER = 'id995002'
HDFS_DATA_ROOT_FOLDER = '/data'
HDFS_CODE_ROOT_FOLDER = '/code'
HDFS_DATA_INGESTION_FOLDER_STRUCTURE = '/data/{{ env }}/raw/{{ app }}'
HDFS_DATA_DELIVERY_FOLDER_STRUCTURE = '/data/{{ env }}/{{ app }}/out'

# ATLAS
ATLAS_SERVER = 'el1538'
ATLAS_PORT = 21000

# AMBARI
AMBARI_SERVER = 'el1538'
AMBARI_PORT = 8080

# WEBHDFS
WEBHDFS_HOST = 'el1538'
WEBHDFS_PORT = 50070

# SECURITY
KERBEROS_ACTIVE = False
