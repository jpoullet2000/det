from det.task import BaseOperator
from det.cli import atlas_client 

class AtlasEntityCreateOperator(BaseOperator):
    """
    Create or updates an entity on Atlas

    Args:
       
      
    Returns:
      
    """
    def __init__(self, **kwargs):
        """It essentially contains the body that will be passed to Atlas to create the entity
        """
        pass 
    def validate_body(self):
        """Validates if the body contains the minimum information to create the Atlas entity
        """
        pass

    def execute(self, context): 
        """Creates or updates existing entity on Atlas
        """
        pass
