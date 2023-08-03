# src\remittances\infraestructure\persistence\database\models\transfer.py

from src.remittances.infraestructure.persistence.database.instance import database_instance as db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from src.shared.ddd.domain.model.Id import Id


class TransferModel(db.Model):
    __tablename__ = 'transfer'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False)
    customer_uuid = db.Column(UUID(as_uuid=True), db.ForeignKey('customer.uuid'), unique=False, nullable=False)
    amount = db.Column(db.Float(precision=2), nullable=False, default=0.00)
    solid_transaction_id = db.Column(db.String,  unique=True, nullable=True)
    ria_transaction_ref = db.Column(db.String,  unique=False, nullable=False)
    destination = db.Column(db.String,  unique=False, nullable=True)
    tx_response = db.Column(db.String,  unique=False, nullable=True)
    code_status = db.Column(db.Integer,  unique=False, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    customer = relationship('CustomerModel', back_populates='transfers')


    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.code_status = 0
        if not self.uuid:
            self.uuid = Id.create().value

