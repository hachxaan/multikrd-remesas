# src/remittances/application/subscribers/transfer_created_subscriber.py

from src.remittances.domain.events.transfer_created_event import TransferCreatedEvent
from src.remittances.domain.repositories.transfer_repository import ITransferRepository
from src.shared.ddd.domain.model.IDomainEvent import IDomainEvent
from src.shared.ddd.domain.model.IDomainEventSubscriber import IDomainEventSubscriber


class TransferCreatedSubscriber(IDomainEventSubscriber):

    def __init__(self, transfer_repository: ITransferRepository):
        self.transfer_repository = transfer_repository

    def handle(self, event: TransferCreatedEvent):
        customer = event.getCustomer()
        self.transfer_repository.save_transfer(customer)


    def isSubscribedTo(self, event: IDomainEvent) -> bool:
        return isinstance(event, TransferCreatedEvent)
