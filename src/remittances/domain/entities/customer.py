# src\customers\domain\entities\customer.py

from typing import List
from src.remittances.domain.entities.transfer import Transfer
from src.shared.ddd.domain.model.EntityRoot import EntityRoot
from src.shared.ddd.domain.model.Id import Id


class Customer(EntityRoot):

    _customerId: Id 
    _user_id: int
    _ria_token: str
    _name: str
    _email: str
    _last_transfer: Transfer
    _transfers: List[Transfer]

    def __init__(self, **kwargs):
        self._customerId = kwargs.get('customerId', None)
        self._user_id = kwargs.get('user_id', None)
        self._ria_token = kwargs.get('ria_token', None)
        self._name = kwargs.get('name', None)
        self._email = kwargs.get('email', None)
        # self._accountBalance = kwargs.get('accountBalance', None)
        # self._accountStatus = kwargs.get('accountStatus', None)
        self._last_transfer = kwargs.get('last_transfer', None)
        self._transfers = kwargs.get('transfers', None)

    @staticmethod
    def createOf(**kwargs) -> 'Customer':
        customer = Customer(**kwargs)
        return customer

    def save(self):
        from src.remittances.domain.events.customer_created import CustomerCreated
        EntityRoot.publishEvent(CustomerCreated(self))

    @property
    def customerId(self) -> Id:
        return self._customerId

    @property
    def ria_token(self):
        return self._ria_token

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

 
    
    @property
    def lastTransfer(self) -> Transfer:
        return self._last_transfers

    @property
    def transfers(self) -> List[Transfer]:
        return self._transfers
