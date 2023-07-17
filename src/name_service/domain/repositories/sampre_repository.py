from typing import List
from abc import ABC, abstractmethod

from src.name_service.domain.entities.sample_entity import SampleEntity
from src.shared.ddd.domain.model.Id import Id


class ISampleRepository(ABC):
    @abstractmethod
    def sample_get_entity(self, id: Id) -> SampleEntity:
        pass

    @abstractmethod
    def sample_save_entity(self, entity_sample: SampleEntity) -> None:
        pass
