# src\remittances\application\subscribers\customer_subscriber.py

from src.remittances.domain.events.customer_created_event import CustomerCreatedEvent
from src.remittances.domain.repositories.customer_repository import ICustomerRepository
from src.shared.ddd.domain.model.IDomainEvent import IDomainEvent
from src.shared.ddd.domain.model.IDomainEventSubscriber import IDomainEventSubscriber


class CustomerCreatedSubscriber(IDomainEventSubscriber):

    def __init__(self, customer_repository: ICustomerRepository):
        self.customer_repository = customer_repository

    def handle(self, event: CustomerCreatedEvent):
        customer_entity = event.getCustomer()
        self.customer_repository.save_customer_entity(customer_entity)

    def isSubscribedTo(self, event: IDomainEvent) -> bool:
        return isinstance(event, CustomerCreatedEvent)
