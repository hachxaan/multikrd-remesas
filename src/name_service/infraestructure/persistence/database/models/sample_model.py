# src\name_service\infraestructure\persistence\database\models\sample_model.py

from src.name_service.infraestructure.persistence.database.instance import database_instance as db
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from src.shared.ddd.domain.model.Id import Id


class SampleModel(db.Model):
    __tablename__ = 'sample'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False)
    sample_property = db.Column(db.String,  unique=False, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if not self.uuid:
            self.uuid = Id.create().value

