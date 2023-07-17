# src\name_service\domain\events\sample_save_entity_event.py


from src.name_service.domain.entities.sample_entity import SampleEntity
from src.shared.ddd.domain.model.DateA import DateA
from src.shared.ddd.domain.model.IDomainEvent import IDomainEvent


class SampleSaveEntityEvent(IDomainEvent):
    """ ev- """

    __occurredOn: DateA
    __sample_entity: SampleEntity

    def __init__(self, sample_entity: SampleEntity) -> None:
        self.__occurredOn = DateA.create()
        self.__sample_entity = sample_entity

    def getSampleEntity(cls) -> SampleEntity:
        return cls.__sample_entity

    @classmethod
    def getOccurredOn(cls) -> DateA:
        return cls.__occurredOn
