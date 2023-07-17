from src.name_service.domain.entities.sample_entity import SampleEntity
from src.name_service.domain.repositories.sampre_repository import ISampleRepository
from src.name_service.infraestructure.persistence.database.models.sample_model import SampleModel
from src.name_service.infraestructure.persistence.database.services.sample_orm_service import SampleORMService
from src.shared.ddd.domain.model.Id import Id
from src.shared.tools.utils import row2dict


class SampleRepositoryAdapter(ISampleRepository):
    def __init__(self, sample_orm_service: SampleORMService):
        self.sample_orm_service = sample_orm_service

    def sample_get_entity(self, id: Id) -> SampleEntity:
        sampleModel = self.sample_orm_service.get_single_sample_model(id)
        return self._convert_model_to_entity(sampleModel)
    
        # Para lista de Modelos
        # return [self._convert_to_domain_entity(sampleModel) for sampleModel in sampleModels]
    
    def sample_save_entity(self, sampleEntity: SampleEntity) -> None:
        self.sample_orm_service.save_sample_model(
            id=sampleEntity.id,
            uuid=str(sampleEntity.uuid.value),
            sample_property=sampleEntity.sample_property,
            createdAt=sampleEntity.createdAt,
        )

    def _convert_model_to_entity(self, infra_biller) -> SampleEntity:
        return SampleEntity(**row2dict(infra_biller))
    


