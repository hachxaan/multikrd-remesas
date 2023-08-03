# src\remittances\domain\entities\transfer.py

from datetime import datetime
from src.shared.ddd.domain.model.EntityRoot import EntityRoot
from src.shared.ddd.domain.model.Id import Id

class Transfer(EntityRoot):
    
    _id: int
    _uuid: Id
    _customer_uuid: Id
    _amount: float
    _solid_transaction_id: str
    _ria_transaction_ref: str
    _destination: str
    _tx_response: str
    _code_status: int
    _created_at: datetime



    def __init__(self, **kwargs):
        self._id = kwargs.get('id', None)
        self._uuid = kwargs.get('uuid', None)
        self._customer_uuid = kwargs.get('customer_uuid', None)
        self._amount = kwargs.get('amount', None)
        self._solid_transaction_id = kwargs.get('solid_transaction_id', None)
        self._ria_transaction_ref = kwargs.get('ria_transaction_ref', None)
        self._destination = kwargs.get('destination', None)
        self._tx_response = kwargs.get('tx_response', None)
        self._code_status = kwargs.get('code_status', None)
        self._created_at = kwargs.get('created_at', None)

    @staticmethod
    def createOf(**kwargs) -> 'Transfer':
        transfer = Transfer(**kwargs)
        return transfer

    # def save(self):
    #     from src.remittances.domain.events.transfer_created_event import TransferCreatedEvent
    #     EntityRoot.publishEvent(TransferCreatedEvent(self))

    @property
    def id(self) -> int:
        return self._id

    @property
    def uuid(self) -> Id:
        return self._uuid

    @property
    def customer_uuid(self) -> Id:
        return self._customer_uuid

    @property
    def amount(self):
        return self._amount

    @property
    def solid_transaction_id(self):
        return self._solid_transaction_id
    
    @property
    def ria_transaction_ref(self):
        return self._ria_transaction_ref

    @property
    def destination(self):
        return self._destination

    @property
    def tx_response(self):
        return self._tx_response

    @property
    def code_status(self):
        return self._code_status

    @property
    def created_at(self):
        return self._created_at
