# src\name_service\domain\entities\sample_entity.py

from datetime import datetime
from src.shared.ddd.domain.model.EntityRoot import EntityRoot
from src.shared.ddd.domain.model.Id import Id


class SampleEntity(EntityRoot):
    def __init__(self, **kwargs):
        self._id =  kwargs.get('id', None)
        self._uuid = Id.create() if not kwargs.get('uuid', None) else Id.ofString(kwargs.get('uuid'))
        self._createdAt = kwargs.get('createdAt', datetime.now())
        self._sample_property = kwargs.get('sample_property', None)
        

    @staticmethod
    def createOf(**kwargs) -> 'SampleEntity':
        return SampleEntity(**kwargs)


    def sample_save_entity(cls):
        from src.name_service.domain.events.sample_save_entity_event import SampleSaveEntityEvent
        EntityRoot.publishEvent(SampleSaveEntityEvent(cls))

    @property
    def id(self) -> int:
        return self._id

    @property
    def uuid(self) -> Id:
        return self._uuid

    @property
    def createdAt(self) -> datetime:
        return self._createdAt
    
    @property
    def sample_property(self) -> str:
        return self._sample_property    
