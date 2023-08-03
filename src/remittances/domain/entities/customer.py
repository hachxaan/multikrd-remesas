# src\customers\domain\entities\customer.py

from typing import Dict, List
from src.remittances.domain.entities.transfer import Transfer
from src.shared.ddd.domain.model.EntityRoot import EntityRoot
from src.shared.ddd.domain.model.Id import Id


class Customer(EntityRoot):

    _id: int
    _customerId: Id 
    _user_id: int
    _ria_token: str
    _email: str
    _mobile_phone: str
    _first_name: str
    _last_name: str
    _last_transfer: Transfer
    _transfers: List[Transfer]

    def __init__(self, **kwargs):
        self._id = kwargs.get('id', None)
        self._customerId = kwargs.get('uuid', Id.create())
        self._user_id = kwargs.get('user_id', None)
        self._ria_token = kwargs.get('ria_token', None)
        self._email = kwargs.get('email', None)
        self._mobile_phone = kwargs.get('mobile_phone', None)
        self._first_name = kwargs.get('first_name', None)
        self._last_name = kwargs.get('last_name', None)
        self._last_transfer = kwargs.get('last_transfer', None)
        self._transfers = kwargs.get('transfers', None)

    @staticmethod
    def createOf(**kwargs) -> 'Customer':
        customer = Customer(**kwargs)
        return customer

    def save(self):
        from src.remittances.domain.events.customer_created_event import CustomerCreatedEvent
        EntityRoot.publishEvent(CustomerCreatedEvent(self))

    def save_token(self, ria_token: str):
        from src.remittances.domain.events.token_saved_event import TokenSavedEvent
        self._ria_token = ria_token
        EntityRoot.publishEvent(TokenSavedEvent(self))        


    def create_transfer(self, **kwargs):
        from src.remittances.domain.events.transfer_created_event import TransferCreatedEvent
        self._last_transfer = Transfer.createOf(
            uuid=Id.create(),
            customer_uuid=self.customerId,
            amount=kwargs.get('amount', 0),
            ria_transaction_ref=kwargs.get('ria_transaction_ref', None),
            destination=kwargs.get('destination', None),
        )
        EntityRoot.publishEvent(TransferCreatedEvent(self))
        
    def set_transfer_code_status(self, code_status: int):
        self.last_transfer._code_status = code_status

    def set_transfer_solid_transaction_id(self, solid_transaction_id: int):
        self.set_transfer_code_status(2)
        self.last_transfer._solid_transaction_id = solid_transaction_id

    def set_transfer_tx_response(self, tx_response: str):
        self.set_transfer_code_status(3)
        self.last_transfer._tx_response = tx_response 

    def send_transfer(self) -> Dict:
        from src.remittances.domain.events.transfer_sent_event import TransferSentEvent
        return EntityRoot.publishEvent(TransferSentEvent(self))


    @property
    def id(self) -> int:
        return self._id
    
    @property
    def customerId(self) -> Id:
        return self._customerId    

    @property
    def ria_token(self):
        return self._ria_token
    
    @property
    def user_id(self):
        return self._user_id  

    @property
    def email(self):
        return self._email
    
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    
    @property
    def last_transfer(self) -> Transfer:
        return self._last_transfer

    @property
    def transfers(self) -> List[Transfer]:
        return self._transfers
