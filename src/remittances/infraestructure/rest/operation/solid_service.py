


from typing import Dict
from src.remittances.infraestructure.microservices.solid.singleton import SolidOperationSingleton
from src.remittances.infraestructure.microservices.solid.solid_transfer import SolidTransfer


class SolidService:

    def __init__(self) -> None:
        self.operation = SolidTransfer(instance=SolidOperationSingleton.instance)

    def transfer_make(
            self, 
            amount: str,
            name: str,
            phone: str,
            email: str
        ) -> Dict:
        return self.operation.transfer_execute(
            amount=amount,
            name=name,
            phone=phone,
            email=email
        )