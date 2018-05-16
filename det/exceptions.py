
def handle_atlas_error(error_message):
    if 'already exists' in error_message:
        response =  'Item already exists: {}'.format(error_message.split('Conflict 409:')[1])
        return response, 409
    else:
        return error_message, 403


class DETException(Exception):
        pass


class DETTaskTimeout(Exception):
        pass
