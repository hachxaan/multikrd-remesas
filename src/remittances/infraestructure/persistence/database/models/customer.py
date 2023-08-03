# src\remittances\infraestructure\persistence\database\models\customer.py

from src.remittances.infraestructure.persistence.database.instance import database_instance as db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from src.shared.ddd.domain.model.Id import Id


class CustomerModel(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=True)
    user_id = db.Column(db.Integer,  unique=True, nullable=False)
    email = db.Column(db.String,  unique=True, nullable=False)
    mobile_phone = db.Column(db.String,  unique=False, nullable=True)
    ria_token = db.Column(db.String,  unique=False, nullable=True)
    first_name = db.Column(db.String,  unique=False, nullable=False)
    last_name = db.Column(db.String,  unique=False, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    
    transfers = relationship('TransferModel', back_populates='customer')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if not self.uuid:
            self.uuid = Id.create().value

