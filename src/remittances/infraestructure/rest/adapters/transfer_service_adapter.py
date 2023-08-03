




from typing import Dict
from src.remittances.domain.adapters.transfer_service_adapter import ITransferServiceAdapter
from src.remittances.domain.entities.customer import Customer
from src.remittances.infraestructure.rest.operation.solid_service import SolidService


class TransferServiceAdapter(ITransferServiceAdapter):
    def __init__(self):
        self.solid_service = SolidService()


    def make_transfer(self, customer: Customer) -> Dict:
        transfer = customer.last_transfer
        return self.solid_service.transfer_make(
            amount=transfer.amount,
            email=customer.email,
            phone=customer.mobile_phone,
            name=f"{customer.first_name} {customer.last_name}"
        )
        