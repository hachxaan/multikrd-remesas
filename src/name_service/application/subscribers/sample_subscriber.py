# src\name_service\application\subscribers\sample_subscriber.py

from src.name_service.domain.events.sample_save_entity_event import SampleSaveEntityEvent
from src.name_service.domain.repositories.sampre_repository import ISampleRepository
from src.shared.ddd.domain.model.IDomainEvent import IDomainEvent
from src.shared.ddd.domain.model.IDomainEventSubscriber import IDomainEventSubscriber


class SampleSubscriber(IDomainEventSubscriber):

    def __init__(self, sample_repository: ISampleRepository):
        self.sample_repository = sample_repository

    def handle(self, event: SampleSaveEntityEvent):
        sample_entity = event.getSampleEntity()


        entities_list = self.sample_repository.sample_save_entity(sample_entity)

        return entities_list

    def isSubscribedTo(self, event: IDomainEvent) -> bool:
        return isinstance(event, SampleSaveEntityEvent)
