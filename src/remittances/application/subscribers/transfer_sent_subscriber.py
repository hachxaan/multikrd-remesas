# src\remittances\application\subscribers\customer_subscriber.py

from src.remittances.domain.adapters.transfer_service_adapter import ITransferServiceAdapter
from src.remittances.domain.events.transfer_sent_event import TransferSentEvent
from src.remittances.domain.repositories.transfer_repository import ITransferRepository
from src.shared.ddd.domain.model.IDomainEvent import IDomainEvent
from src.shared.ddd.domain.model.IDomainEventSubscriber import IDomainEventSubscriber


class TransferSentSubscriber(IDomainEventSubscriber):

    def __init__(
            self, 
            transfer_service: ITransferServiceAdapter,
            transfer_repository: ITransferRepository):
        self.transfer_service = transfer_service
        self.transfer_repository = transfer_repository

    def handle(self, event: TransferSentEvent):
        customer = event.getCustomer()
        customer.set_transfer_code_status(1)
        self.transfer_repository.update_sent_transfer(
            transfer_entity=customer.last_transfer
        )
        response = self.transfer_service.make_transfer(event.getCustomer())

        if response.get('statusCode') == 200:
            customer.set_transfer_solid_transaction_id(
                response.get('data')['transactionId']
            )
            self.transfer_repository.update_success_transfer(customer.last_transfer)
        else:
            customer.set_transfer_tx_response(
                response.get('data')['message']
            )
            self.transfer_repository.update_fail_transfer(customer.last_transfer)

        return response

    def isSubscribedTo(self, event: IDomainEvent) -> bool:
        return isinstance(event, TransferSentEvent)
