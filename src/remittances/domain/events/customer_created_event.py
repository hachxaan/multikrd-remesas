# src\billcustomers\domain\events\customer_created_event.py

from src.remittances.domain.entities.customer import Customer
from src.shared.ddd.domain.model.DateA import DateA
from src.shared.ddd.domain.model.IDomainEvent import IDomainEvent


class CustomerCreatedEvent(IDomainEvent):
    """ ev- """

    __occurredOn: DateA
    __customer: Customer

    def __init__(self, customer: Customer) -> None:
        self.__occurredOn = DateA.create()
        self.__customer = customer

    def getCustomer(cls) -> Customer:
        return cls.__customer

    @classmethod
    def getOccurredOn(cls) -> DateA:
        return cls.__occurredOn
