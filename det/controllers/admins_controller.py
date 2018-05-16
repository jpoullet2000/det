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
    if connexion.request.is_json:
        Typedefs = TypedefsItem.from_dict(connexion.request.get_json())  # noqa: E501
        from det.operators.atlas_typedefs_create import AtlasTypedefsCreateOperator
        atlas_typedefs_operator = AtlasTypedefsCreateOperator(typedefs=Typedefs, body_json=connexion.request.get_json())
        message = atlas_typedefs_operator.execute()
    return message  
    #return 'Please enter a correct json string'
