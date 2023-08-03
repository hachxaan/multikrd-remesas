#src/remittances/domain/events/transfer_succeeded_event.py

from src.remittances.domain.entities.transfer import Customer
from src.shared.ddd.domain.model.DateA import DateA
from src.shared.ddd.domain.model.IDomainEvent import IDomainEvent


class TransferFailedEvent(IDomainEvent):
    """ ev- """

    __occurredOn: DateA
    __transfer: Customer

    def __init__(self, transfer: Customer) -> None:
        self.__occurredOn = DateA.create()
        self.__transfer = transfer

    def getTransfer(cls) -> Customer:
        return cls.__transfer

    @classmethod
    def getOccurredOn(cls) -> DateA:
        return cls.__occurredOn