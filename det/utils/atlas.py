from det.app import ATLAS_CLIENT


class Atlas():
    """Utils to get info from the Atlas API 
    """
    def __init__(self, atlas_client=ATLAS_CLIENT):
        """
        """
        self.atlas_client = atlas_client

    def get_classification_defs(self):
        classifications = []
        for typedefs in self.atlas_client.typedefs:
            for classification_def in typedefs.classificationDefs:
                classification = {}
                for field in classification_def.fields:
                    classification[field] = getattr(classification_def, field)
                classification['attributeDefs'] = []
                for attribute in classification_def.attributeDefs:
                    classification['attributeDefs'].append(attribute._data)
                classifications.append(classification)
        return classifications
    
    def get_entity_defs(self):
        entities = []
        for typedefs in self.atlas_client.typedefs:
            for entity_def in typedefs.entityDefs:
                entity = {}
                for field in entity_def.fields:
                    entity[field] = getattr(entity_def, field)
                entity['attributeDefs'] = []
                for attribute in entity_def.attributeDefs:
                    entity['attributeDefs'].append(attribute._data)
                entities.append(entity)
        return entities
    
    def get_enum_defs(self):
        enums = []
        for typedefs in self.atlas_client.typedefs:
            for enum_def in typedefs.enumDefs:
                enum = {}
                for field in enum_def.fields:
                    enum[field] = getattr(enum_def, field)
                enum['elementDefs'] = []
                for element in enum_def.elementDefs:
                    enum['elementDefs'].append(element._data)
                enums.append(enum)
        return enums
