from abc import ABC, abstractmethod
from typing import Dict

from src.remittances.domain.entities.customer import Customer


class ITransferServiceAdapter(ABC):


    @abstractmethod
    def make_transfer(self, customer: Customer) -> Dict:
        pass    
