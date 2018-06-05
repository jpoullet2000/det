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

    def get_typedefs_not_in_atlas(self):
        """ Check in Atlas if the typedefs already exist and returns a json with only those that are not yet in Atlas
        """
        existing_entitydefs_names = []
        existing_enumdefs_names = []
        existing_classificationdefs_names = []
        for typedef in ATLAS_CLIENT.typedefs:
            existing_entitydefs_names = [entity.name for entity in typedef.entityDefs]
            existing_enumdefs_names = [enum.name for enum in typedef.enumDefs]
            existing_classificationdefs_names = [classification.name for classification in typedef.classificationDefs]
        new_body = dict() 
        if 'enitityDefs' in self.body_json:
            new_body['entityDefs'] = list()
            for entity in self.body_json['entityDefs']:
                if entity['name'] not in existing_entitydefs_names:
                    new_body['entityDefs'].append(entity)
            if len(new_body['entityDefs']) == 0:
                del new_body['entityDefs']
        if 'classificationDefs' in self.body_json:
            new_body['classificationDefs'] = list()
            for classification in self.body_json['classificationDefs']:
                if classification['name'] not in existing_classificationdefs_names:
                    new_body['classificationDefs'].append(classification)
            if len(new_body['classificationDefs']) == 0:
                del new_body['classificationDefs']
        if 'enumDefs' in self.body_json:
            new_body['enumDefs'] = list()
            for enum in self.body_json['enumDefs']:
                if enum['name'] not in existing_enumdefs_names:
                    new_body['enumDefs'].append(enum)
            if len(new_body['enumDefs']) == 0:
                del new_body['enumDefs']
        return new_body


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
            self.body_not_yet_in_atlas = self.get_typedefs_not_in_atlas()
            if len(self.body_not_yet_in_atlas) == 0:
                return 'All typedefs already exist!'
            ATLAS_CLIENT.typedefs.create(data=self.body_not_yet_in_atlas)
            #ATLAS_CLIENT.typedefs.create(data=self.body_json)
            return 'Typedef has been created successfully!'
        except:
            return handle_atlas_error(traceback.format_exc())
