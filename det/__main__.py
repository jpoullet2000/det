#!/usr/bin/env python

import connexion
from connexion.resolver import RestyResolver

from det import encoder


def main():
    print(__name__)
    app = connexion.App('det', specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', resolver=RestyResolver('det'), arguments={'packageName': 'det', 'title': 'Data engineering toolkit API'}) #  resolver=RestyResolver('.'), 
    app.run(port=8080)


if __name__ == '__main__':
    main()
