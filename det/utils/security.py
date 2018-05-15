import logging

from credentials import credentials 
from flask import request
from functools import wraps 


def get_credentials(cred_vars):
    """
    Get credentials from $HOME/.credentials.json
    Args:
       cred_vars(list): list of credential variables
    Returns:
      creds(dict): dictionary of credentials
    """ 
    creds = dict()
    try: 
        _creds = credentials.require(cred_vars)
        for var in cred_vars:
            creds[var] = getattr(_creds, var)
        return creds
    except:
        return None


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None
        creds = get_credentials(['TEST_FLAG', 'DET_API_ADMIN_TOKEN'])
        if 'TEST_FLAG' in creds and creds['TEST_FLAG']:
            return f(*args, **kwargs)
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message' : 'Token is missing.'}, 401
        
        if token != creds['DET_API_ADMIN_TOKEN']:
            return {'message' : 'Your token is wrong, wrong, wrong!!!'}, 401

        return f(*args, **kwargs)

    return decorated

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None
        creds = get_credentials(['TEST_FLAG', 'DET_API_TOKEN'])
        if 'TEST_FLAG' in creds and creds['TEST_FLAG']:
            return f(*args, **kwargs)
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message' : 'Token is missing.'}, 401
        
        if token != creds['DET_API_TOKEN']:
            return {'message' : 'Your token is wrong, wrong, wrong!!!'}, 401

        return f(*args, **kwargs)

    return decorated
