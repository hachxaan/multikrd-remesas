# src\name_service\application\services\sample_service.py


from src.name_service.domain.entities.sample_entity import SampleEntity
from src.shared.tools.errors.project_exception import ProjectException



class SampleCreateEntityService:

    def __init__(self, sample_property: str):
        self.sample_property = sample_property
        
    
    def execute(self):
        try:

            sample_entity = SampleEntity.createOf(
                sample_property=self.sample_property
            )
            sample_entity.sample_save_entity()

        except Exception as e:
            raise ProjectException(f"Error: {str(e)}")
