# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO
from unittest.mock import Mock

from det.models.typedefs_item import TypedefsItem  # noqa: E501
from det import __version__

from det.operators.atlas_typedefs_create import AtlasTypedefsCreateOperator
from . import BaseTestCase


class TestAdminsController(BaseTestCase):
    """AdminsController integration test stubs"""

    def test_add_typedefs(self):
        """Test case for add_typedefs

        create type definitions
        """
        MockTypedefsCreateOperator = AtlasTypedefsCreateOperator
        MockTypedefsCreateOperator.execute = Mock(return_value=False)
        Typedefs = TypedefsItem()
        response = self.client.open(
            '/detapi/{version}/typedefs'.format(version=__version__),
            method='POST',
            data=json.dumps(Typedefs),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
