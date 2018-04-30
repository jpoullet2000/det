import logging

from credentials import credentials 


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
