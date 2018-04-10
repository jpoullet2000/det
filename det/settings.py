import os
import socket

if 'DET_HOME' not in os.environ:
    os.environ['DET_HOME'] = os.path.join(os.path.expanduser('~'), '.det')

if not os.path.exists(os.environ['DET_HOME']):
    os.makedirs(os.environ['DET_HOME']) 

# DET
DET_WEBSERVER_PORT = 8888
DET_WEBSERVER_PORT_DEV = 8889
DET_WEBSERVER_ADDRESS = 'localhost' #'{}'.format(socket.gethostname())
DET_WEBSERVER_TIMEOUT = 45
DET_WORKERS = 2

# ATLAS
ATLAS_SERVER = 'el1538'
ATLAS_PORT = 21000

# SECURITY
KERBEROS_ACTIVE = True
