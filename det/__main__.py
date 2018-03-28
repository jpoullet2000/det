#!/usr/bin/env python

from credentials import credentials 
from atlasclient.client import Atlas

import os 

import connexion
from connexion.resolver import RestyResolver

from det import encoder

CONFIG_MODULE = os.environ.get('DET_CONFIG', 'det.settings')

creds = credentials.require(['atlas_login', 'atlas_password'])


def main():
    app = connexion.App('det', specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.app.config.from_object(CONFIG_MODULE)
    conf = app.app.config
    app.add_api('swagger.yaml', resolver=RestyResolver('det'), arguments={'packageName': 'det', 'title': 'Data engineering toolkit API'}) 
    app.run(port=app.app.config['DET_WEBSERVER_PORT'])
    atlas_client = Atlas(conf['ATLAS_SERVER', port=conf['ATLAS_PORT'], username=creds.atlas_login, password=creds.atlas_password)

if __name__ == '__main__':
    main()
