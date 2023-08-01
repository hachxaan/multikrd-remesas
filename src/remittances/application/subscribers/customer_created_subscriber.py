# src\remittances\application\subscribers\customer_subscriber.py

from src.remittances.domain.events.customer_created import CustomerCreated
from src.remittances.domain.repositories.customer_repository import ICustomerRepository
from src.shared.ddd.domain.model.IDomainEvent import IDomainEvent
from src.shared.ddd.domain.model.IDomainEventSubscriber import IDomainEventSubscriber


class CustomerCreatedSubscriber(IDomainEventSubscriber):

    def __init__(self, customer_repository: ICustomerRepository):
        self.customer_repository = customer_repository

    def handle(self, event: CustomerCreated):
        customer_entity = event.getCustomerEntity()


        entities_list = self.customer_repository.customer_save_entity(customer_entity)

        return entities_list

    def isSubscribedTo(self, event: IDomainEvent) -> bool:
        return isinstance(event, CustomerCreated)
