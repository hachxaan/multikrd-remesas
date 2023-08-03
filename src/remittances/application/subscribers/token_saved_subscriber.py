# src\remittances\application\subscribers\customer_subscriber.py

from src.remittances.domain.events.token_saved_event import TokenSavedEvent
from src.remittances.domain.repositories.customer_repository import ICustomerRepository
from src.shared.ddd.domain.model.IDomainEvent import IDomainEvent
from src.shared.ddd.domain.model.IDomainEventSubscriber import IDomainEventSubscriber


class TokenSavedSubscriber(IDomainEventSubscriber):

    def __init__(self, customer_repository: ICustomerRepository):
        self.customer_repository = customer_repository

    def handle(self, event: TokenSavedEvent):
        self.customer_repository.save_token(event.getCustomer())

    def isSubscribedTo(self, event: IDomainEvent) -> bool:
        return isinstance(event, TokenSavedEvent)
