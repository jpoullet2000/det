import connexion
import six

from swagger_server.models.typedefs_item import TypedefsItem  # noqa: E501
from swagger_server import util


def add_typedefs(Typedefs=None):  # noqa: E501
    """create type definitions

    Create type definitions # noqa: E501

    :param Typedefs: Typedefs
    :type Typedefs: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Typedefs = TypedefsItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
