from abc import ABC, abstractmethod

from src.remittances.domain.entities.customer import Customer
from src.remittances.domain.entities.transfer import Transfer
from src.shared.ddd.domain.model.Id import Id


class ITransferRepository(ABC):


    @abstractmethod
    def save_transfer(self, customer_entity: Customer) -> None:
        pass    

    @abstractmethod
    def update_sent_transfer(self, transfer_entity: Transfer) -> None:
        pass

    @abstractmethod
    def update_success_transfer(self, transfer_entity: Transfer) -> None:
        pass

    @abstractmethod
    def update_fail_transfer(self, transfer_entity: Transfer) -> None:
        pass