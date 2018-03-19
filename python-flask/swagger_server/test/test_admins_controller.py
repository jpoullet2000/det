# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.typedefs_item import TypedefsItem  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdminsController(BaseTestCase):
    """AdminsController integration test stubs"""

    def test_add_typedefs(self):
        """Test case for add_typedefs

        create type definitions
        """
        Typedefs = TypedefsItem()
        response = self.client.open(
            '/jpoullet2000/detapi/0.0.1/typedefs',
            method='POST',
            data=json.dumps(Typedefs),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
