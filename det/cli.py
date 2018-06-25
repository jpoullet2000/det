#!/usr/bin/env python

from subprocess import Popen
import os 
from colorama import Fore, Style

from credentials import credentials 
from atlasclient.client import Atlas
from ambariclient.client import Ambari

import connexion
from connexion.resolver import RestyResolver
from flask_script import Manager 

from det.app import APP


conf = APP.app.config
manager = Manager(APP.app)


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
        APP.run(port=port)
    else:
        addr_str = '{address}:{port} '
        cmd = (
            'gunicorn '
            '-w {workers} '
            '--timeout {timeout} '
            '-b ' + addr_str +
            '--limit-request-line 0 '
            '--limit-request-field_size 0 '
            'det.cli:APP').format(**locals())
        print(Fore.GREEN + 'Starting server with command: ')
        print(Fore.YELLOW + cmd)
        print(Style.RESET_ALL)
        Popen(cmd, shell=True).wait()
