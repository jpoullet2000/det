#!/usr/bin/env python

from credentials import credentials 
from atlasclient.client import Atlas

import os 
import logging 

import connexion
from connexion.resolver import RestyResolver
from flask_script import Manager 

from det import encoder

CONFIG_MODULE = os.environ.get('DET_CONFIG', 'det.settings')

try: 
    creds = credentials.require(['atlas_login', 'atlas_password'])
    atlas_login = creds.atlas_login
    atlas_password = creds.atlas_password
except:
    atlas_login = 'atlas_login'
    atlas_password = 'atlas_password'

app = connexion.App('det', specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.app.config.from_object(CONFIG_MODULE)
conf = app.app.config
app.add_api('swagger.yaml', resolver=RestyResolver('det'), arguments={'packageName': 'det', 'title': 'Data engineering toolkit API'}) 
manager = Manager(app.app)

@manager.option(
        '-d', '--debug', action='store_true',
        help='Start the web server in debug mode')
def runserver(debug=False):
    """Starts the det webserver"""
    app.run(port=conf['DET_WEBSERVER_PORT'])
    atlas_client = Atlas(conf['ATLAS_SERVER'], port=conf['ATLAS_PORT'], username=atlas_login, password=atlas_password)
