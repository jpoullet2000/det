#!/usr/bin/env python

from credentials import credentials 
from atlasclient.client import Atlas
from ambariclient.client import Ambari
from colorama import Fore, Style

from subprocess import Popen
import os 
import logging 

import connexion
from connexion.resolver import RestyResolver
from flask_script import Manager 

from det import encoder
from det.utils.hdfs import HDFS
from det.utils.security import get_credentials

CONFIG_MODULE = os.environ.get('DET_CONFIG', 'det.settings')

#try: 
#    _creds = credentials.require(['atlas_login', 'atlas_password', 'ambari_login', 'ambari_password'])
#    atlas_login = _creds.atlas_login
#    atlas_password = _creds.atlas_password
#except:
#    atlas_login = 'atlas_login'
#    atlas_password = 'atlas_password'
#    ambari_login = 'ambari_login'
#    ambari_password = 'ambari_password'

app = connexion.App('det', specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.app.config.from_object(CONFIG_MODULE)
conf = app.app.config
app.add_api('swagger.yaml', resolver=RestyResolver('det'), arguments={'packageName': 'det', 'title': 'Data engineering toolkit API'}) 
manager = Manager(app.app)

cred_vars = ['ATLAS_LOGIN', 
             'ATLAS_PASSWORD', 
             'AMBARI_LOGIN', 
             'AMBARI_PASSWORD']
creds = get_credentials(cred_vars)
if not creds:
    logging.info('Using test credentials')
    creds = dict()
    for var in cred_vars:
        creds[var] = conf['TEST_{}'.format(var)]
atlas_client = Atlas(conf['ATLAS_SERVER'], port=conf['ATLAS_PORT'], username=creds['ATLAS_LOGIN'], password=creds['ATLAS_PASSWORD'])
ambari_client = Ambari(conf['AMBARI_SERVER'], port=conf['AMBARI_PORT'], username=creds['AMBARI_LOGIN'], password=creds['AMBARI_PASSWORD']) 
hdfs_client = HDFS(webhdfs_host=conf['WEBHDFS_HOST'], webhdfs_port=conf['WEBHDFS_PORT'])

@manager.option(
        '-d', '--debug', action='store_true',
        help='Start the web server in debug mode')
@manager.option(
    '-a', '--address', default=conf['DET_WEBSERVER_ADDRESS'],
    help='Specify the address to which to bind the web server')
@manager.option(
    '-p', '--port', default=conf['DET_WEBSERVER_PORT'],
    help='Specify the port on which to run the web server')
@manager.option(
    '-w', '--workers',
    default=conf.get('DET_WORKERS', 2),
    help='Number of gunicorn web server workers to fire up')
@manager.option(
    '-t', '--timeout', default=conf.get('DET_WEBSERVER_TIMEOUT'),
help='Specify the timeout (seconds) for the gunicorn web server')
def runserver(debug, address, port, workers, timeout):
    """Starts the det webserver"""
    if debug:
        print(
              Fore.YELLOW + 'Starting DET server in ' +
              Fore.RED + 'DEBUG' +
              Fore.YELLOW + ' mode')
        print(Fore.BLUE + '-=' * 20)
        print(Style.RESET_ALL)
        app.run(port=conf['DET_WEBSERVER_PORT'])
    else:
        addr_str = '{address}:{port} '
        cmd = (
            'gunicorn '
            '-w {workers} '
            '--timeout {timeout} '
            '-b ' + addr_str +
            '--limit-request-line 0 '
            '--limit-request-field_size 0 '
            'det.cli:app').format(**locals())
        print(Fore.GREEN + 'Starting server with command: ')
        print(Fore.YELLOW + cmd)
        print(Style.RESET_ALL)
        Popen(cmd, shell=True).wait()
