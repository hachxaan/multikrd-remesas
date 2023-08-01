# src\remittances\infraestructure\persistence\adapters\customer_persistence_adapter.py

from src.remittances.infraestructure.persistence.database.models.customer import CustomerModel
from src.remittances.infraestructure.persistence.database.models.transfer import TransferModel
from src.remittances.domain.entities.customer import Customer
from src.remittances.domain.entities.transfer import Transfer
from src.remittances.domain.repositories.customer_repository import ICustomerRepository
from src.remittances.infraestructure.persistence.database.services.customer_orm_service import CustomerORMService
from src.shared.ddd.domain.model.Id import Id
from src.shared.tools.utils import row2dict


class CustomerRepositoryAdapter(ICustomerRepository):
    def __init__(self, customer_orm_service: CustomerORMService):
        self.customer_orm_service = customer_orm_service

    def get_entity_by_user_id(self, user_id: int) -> Customer:
        customerModel = self.customer_orm_service.get_by_user_id(user_id)
        return self._convert_customer_model_to_entity(customerModel)
    
    
    def get_entity_by_user_id_with_last_transfer(self, user_id: int) -> Customer:
        customerModel, lastTransferModel = self.customer_orm_service.get_by_user_id(user_id)
        lastTransferEntity = self._convert_transfer_model_to_entity(lastTransferModel) if lastTransferModel else None

        return self._convert_customer_model_to_entity(customerModel, lastTransferEntity)
    
    def get_entity_by_uuid(self, uuid: Id) -> Customer:
        pass

    def get_entity_by_uuid_with_last_transfer(self, uuid: Id) -> Customer:
        pass        

    def get_entity_by_token(self, ria_token: str) -> Customer:
        pass

    def save_customer_entity(self, customer_entity: Customer) -> None:
        pass

    def _convert_customer_model_to_entity(self, customer_model: CustomerModel, transfer : Transfer = None) -> Customer:
        cutomer_dict = row2dict(customer_model)
        cutomer_dict['last_transfer'] = transfer
        return Customer(**cutomer_dict)

    def _convert_transfer_model_to_entity(self, transfer_model: TransferModel) -> Transfer:
        return Transfer(**row2dict(transfer_model))
    


