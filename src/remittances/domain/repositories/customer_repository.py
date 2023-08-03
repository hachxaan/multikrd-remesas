from abc import ABC, abstractmethod

from src.remittances.domain.entities.customer import Customer
from src.shared.ddd.domain.model.Id import Id


class ICustomerRepository(ABC):
    @abstractmethod
    def get_entity_by_user_id(self, user_id: int) -> Customer:
        pass

    @abstractmethod
    def get_entity_by_user_id_with_last_transfer(self, user_id: int) -> Customer:
        pass

    @abstractmethod
    def get_entity_by_uuid(self, uuid: Id) -> Customer:
        pass

    @abstractmethod
    def get_entity_by_uuid_with_last_transfer(self, uuid: Id) -> Customer:
        pass    

    @abstractmethod
    def get_entity_by_token(self, ria_token: str) -> Customer:
        pass    

    @abstractmethod
    def save_customer_entity(self, customer_entity: Customer) -> None:
        pass

    @abstractmethod
    def save_token(self, customer_entity: Customer) -> None:
        pass    
