import connexion
import six
import json

from det.models.typedefs_item import TypedefsItem  # noqa: E501
from det import util
from det.utils.security import admin_token_required


@admin_token_required
def add_typedefs(Typedefs=None):  # noqa: E501
    """create type definitions

    Create type definitions # noqa: E501

    :param Typedefs: Typedefs
    :type Typedefs: dict | bytes

    :rtype: None
    """
#    from det.app import ATLAS_CLIENT
    if connexion.request.is_json:
        Typedefs = TypedefsItem.from_dict(connexion.request.get_json())  # noqa: E501
#    ATLAS_CLIENT.typedefs.create(data=connexion.request.get_json())
#    return 'Typedefs have been created'
    return 'Not yet implemented'
