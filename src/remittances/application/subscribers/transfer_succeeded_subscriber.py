# src/remittances/application/subscribers/transfer_created_subscriber.py

from src.remittances.domain.adapters.transfer_service_adapter import ITransferServiceAdapter
from src.remittances.domain.events.transfer_succeeded_event import TransferSucceededEvents
from src.remittances.domain.repositories.transfer_repository import ITransferRepository
from src.shared.ddd.domain.model.IDomainEvent import IDomainEvent
from src.shared.ddd.domain.model.IDomainEventSubscriber import IDomainEventSubscriber


class TransferSucceededSubscriber(IDomainEventSubscriber):

    def __init__(
            self, 
            transfer_repository: ITransferRepository,
            transef_service_adapter: ITransferServiceAdapter
        ):
        self.transfer_repository = transfer_repository
        self.transfer_service_adapter = transef_service_adapter

    def handle(self, event: TransferSucceededEvents):
        transfer = event.getTransfer()

        response = self.transfer_service_adapter.make_transfer(
            transfer=transfer
        )

        

        if response.get('codeStatus') == 200:
            transfer.code_status = 1
            transfer.solid_transaction_id = response.get('data').get('transactionId')
            self.transfer_repository.update_success_transfer(
                transfer_entity=transfer
            )
            
        else:
            transfer.code_status = 2
            transfer.tx_response = \
                f'EC_TRANSFER_INSUFF_DEST_BALANCE: Available balance: {response.get("data").get("availableBalance")}'
            self.transfer_repository.update_fail_transfer(
                transfer_entity=transfer
            )
    
        return response

    def isSubscribedTo(self, event: IDomainEvent) -> bool:
        return isinstance(event, TransferSucceededEvents)
