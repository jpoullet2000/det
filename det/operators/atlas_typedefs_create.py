from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import json
import logging
import sys
import traceback

from det.app import ATLAS_CLIENT 
from det.exceptions import DETException
from det.task import BaseOperator
from det.exceptions import handle_atlas_error

class AtlasTypedefsCreateOperator(BaseOperator):
    """
    Create typedefs on Atlas (it cannot update existing ones)
    """
    def __init__(self, typedefs, body_json, **kwargs):
        """It uses the typedefs model and validate the content before sending it to Atlas

        Args:
           typedefs(Typedefs): Typedefs object with info to create the typedefs in Atlas
           bodyjson(str): Body in json format as given as body when calling the API
        """
        self.typedefs = typedefs 
        self.body_json = body_json
        self.types = ['classification_defs', 'enum_defs', 'entity_defs']

    def exist_typedefs(self, typedef_name):
        """ Check in Atlas if the typedef already exists
        """
        pass


    def validate_body(self):
        """Validates if the body contains the minimum information to create the Atlas typedefs
          
        """
        if all(getattr(self.typedefs, a) is None for a in self.types):
            error_message = 'A typedefs should be one of the items: classificationDefs, entityDefs, enumDefs'
            raise DETException(error_message)
        return True

    def execute(self, context=None): 
        """Creates or updates existing entity on Atlas
        """
        if not self.validate_body:
            error_message = 'The body is not correct.'
            return error_message, 403
        try: 
            ATLAS_CLIENT.typedefs.create(data=self.body_json)
            return 'Typedef has been created successfully!'
        except:
            return handle_atlas_error(traceback.format_exc())
