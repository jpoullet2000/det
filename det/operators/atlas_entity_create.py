import json

from det.task import BaseOperator
from det.cli import atlas_client 
from det.exceptions import DETException

class AtlasEntityCreateOperator(BaseOperator):
    """
    Create or updates an entity on Atlas
    """
    def __init__(self, attributes, classifications=None, referred_entities=None, entity_type=None, **kwargs):
        """It essentially contains the info to create the body that will be passed to Atlas to create the entity

        Args:
           attributes(dict): dictionary of attributes as defined in Apache Atlas
           classifications(list): list of classifications or tags as defined in Apache Atlas
           referred_entities(dict): dictionary of referred entities as defined in Atlas 
           entity_type(str): entity type (e.g. hdfs_path, hbase_column, etc) to validate that minimum info is provided to create the entity in Atlas 
        """
        self.attributes = attributes
        self.classifications = classifications
        self.referred_entities = referred_entities
        self.entity_type = entity_type

    @property
    def body(self):
        if not self.validate_body():
            return None
        entity_data = {'entity': {'attributes': {}}}
        for attribute in self.attributes:
            entity_data['entity']['attributes'][attribute] = self.attributes[attribute]
        if self.classifications:
            entity_data['entity']['classifications'] = self.classifications
        body = json.dumps(entity_data)
        return body

    def validate_body(self):
        """Validates if the body contains the minimum information to create the Atlas entity
        """
        if 'qualifiedName' not in self.attributes:
            error_message = 'The attribute "qualified_name" must be defined'
            raise DETException(error_message)
        if self.entity_type and self.entity_type == 'hdfs_path' and 'path' not in self.attributes:
            error_message = 'The attribute "path" must be defined'
            raise DETException(error_message)
        return True

    def execute(self, context=None): 
        """Creates or updates existing entity on Atlas
        """
        if not self.body:
            error_message = 'The body could not be created. Info is missing'
            raise DETException(error_message)
        atlas_client.entity_post.create(data=self.body)
