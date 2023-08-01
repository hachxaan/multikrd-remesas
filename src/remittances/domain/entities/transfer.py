# src\remittances\domain\entities\transfer.py

from src.shared.ddd.domain.model.EntityRoot import EntityRoot

class Transfer(EntityRoot):
    def __init__(self, **kwargs):
        self._id = kwargs.get('id', None)
        self._uuid = kwargs.get('uuid', None)
        self._customer_uuid = kwargs.get('customer_uuid', None)
        self._user_id = kwargs.get('user_id', None)
        self._amount = kwargs.get('amount', None)
        self._transaction_id = kwargs.get('transaction_id', None)
        self._destination = kwargs.get('destination', None)
        self._tx_response = kwargs.get('tx_response', None)
        self._code_status = kwargs.get('code_status', None)
        self._created_at = kwargs.get('created_at', None)

    @staticmethod
    def createOf(**kwargs) -> 'Transfer':
        transfer = Transfer(**kwargs)
        return transfer

    def save(self):
        from src.remittances.domain.events.transfer_created import TransferCreated
        EntityRoot.publishEvent(TransferCreated(self))

    @property
    def id(self):
        return self._id

    @property
    def uuid(self):
        return self._uuid

    @property
    def customer_uuid(self):
        return self._customer_uuid

    @property
    def user_id(self):
        return self._user_id

    @property
    def amount(self):
        return self._amount

    @property
    def transaction_id(self):
        return self._transaction_id

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
