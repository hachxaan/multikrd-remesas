# src\remittances\infraestructure\persistence\adapters\customer_persistence_adapter.py

from src.remittances.domain.entities.customer import Customer
from src.remittances.domain.entities.transfer import Transfer
from src.remittances.domain.repositories.transfer_repository import ITransferRepository
from src.remittances.infraestructure.persistence.database.services.transfer_orm_service import TransferORMService
from src.shared.ddd.domain.model.Id import Id


class TransferRepositoryAdapter(ITransferRepository):
    def __init__(self, transfer_orm_service: TransferORMService):
        self.transfer_orm_service = transfer_orm_service

    def save_transfer(self, customer_entity: Customer) -> None:

        transfer_entity = customer_entity._last_transfer
        
        self.transfer_orm_service.save_transfer(transfer_data={
            'uuid': transfer_entity.uuid.value,
            'customer_uuid': str(customer_entity.customerId.value),
            'amount': transfer_entity.amount,
            'ria_transaction_ref': transfer_entity.ria_transaction_ref,
            'destination': transfer_entity.destination
        })

    def update_sent_transfer(self, transfer_entity: Transfer) -> None:
        self.transfer_orm_service.update_transfer(
            transfer_data={
                'uuid': transfer_entity.uuid,
                'code_status': transfer_entity.code_status,
            }
        )

    def update_success_transfer(self, transfer_entity: Transfer) -> None:
        self.transfer_orm_service.update_transfer(
            transfer_data={
                'uuid': transfer_entity.uuid,
                'code_status': transfer_entity.code_status,
                'solid_transaction_id': transfer_entity.solid_transaction_id
            }
        )

    def update_fail_transfer(self, transfer_entity: Transfer) -> None:
        self.transfer_orm_service.update_transfer(
            transfer_data={
                'uuid': transfer_entity.uuid,
                'code_status': transfer_entity.code_status,
                'tx_response': transfer_entity.tx_response
            }
        )        