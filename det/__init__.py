#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import  print_function
from __future__ import unicode_literals

import os
from pkg_resources import resource_filename
from credentials import credentials 
from atlasclient.client import Atlas
from ambariclient.client import Ambari

import connexion
from connexion.resolver import RestyResolver

from det import encoder
from det.utils.security import get_credentials
from det.utils.hdfs import HDFS


__version__ = '0.0.3'

CONFIG_MODULE = os.environ.get('DET_CONFIG', 'det.settings')

APP = connexion.App('det', specification_dir=resource_filename(__name__, 'swagger'))
APP.app.json_encoder = encoder.JSONEncoder
APP.app.config.from_object(CONFIG_MODULE)
conf = APP.app.config
APP.add_api('swagger.yaml', resolver=RestyResolver('det'), arguments={'packageName': 'det', 'title': 'Data engineering toolkit API'}) 

cred_vars = ['ATLAS_LOGIN', 
             'ATLAS_PASSWORD', 
             'AMBARI_LOGIN', 
             'AMBARI_PASSWORD']
CREDS = get_credentials(cred_vars)
if not CREDS:
    logging.info('Using test credentials')
    CREDS = dict()
    for var in cred_vars:
        CREDS[var] = conf['TEST_{}'.format(var)]
ATLAS_CLIENT = Atlas(conf['ATLAS_SERVER'], 
                     port=conf['ATLAS_PORT'], 
                     username=CREDS['ATLAS_LOGIN'], 
                     password=CREDS['ATLAS_PASSWORD'],
                     timeout=180000)
AMBARI_CLIENT = Ambari(conf['AMBARI_SERVER'], 
                       port=conf['AMBARI_PORT'], 
                       username=CREDS['AMBARI_LOGIN'], 
                       password=CREDS['AMBARI_PASSWORD']) 
HDFS_CLIENT = HDFS(webhdfs_host=conf['WEBHDFS_HOST'], webhdfs_port=conf['WEBHDFS_PORT'])
