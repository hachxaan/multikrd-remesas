# src\name_service\infraestructure\persistence\database\services\biller_orm_service.py

from typing import List
from sqlalchemy.exc import SQLAlchemyError
from src.name_service.domain.entities.sample_entity import SampleEntity
from src.name_service.infraestructure.persistence.classes.meta_service import MetaService
from src.name_service.infraestructure.persistence.database.instance import database_instance as db
from src.name_service.infraestructure.persistence.database.models.sample_model import SampleModel
from src.shared.ddd.domain.model.Id import Id


class SampleORMService(MetaService):
    def __init__(self):
        self.session = db.session

    @classmethod
    def get_all_sample_model(self) -> List[SampleModel]:
        try:
            return self.session.query(SampleModel).order_by(
                SampleModel.id
            ).all()
        except SQLAlchemyError as e:
            print(f"Ha ocurrido un error de SQLAlchemy: {str(e)}")
            return None
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {str(e)}")
            return None
    
    @classmethod
    def get_single_sample_model(self, id: Id) -> SampleModel:
        try:
            filters = {'uuid': id.value}
            sampleModel = SampleModel.query.filter_by(
                **filters
            ).first()
            return sampleModel
        except SQLAlchemyError as e:
            print(f"Ha ocurrido un error de SQLAlchemy: {str(e)}")
            return None
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {str(e)}")
            return None
        
    @classmethod
    def save_sample_model(cls, **kwargs):
        try:
            sample_model = SampleModel(
                id=kwargs.get('id', None),
                uuid=kwargs.get('uuid', None),
                sample_property=kwargs.get('sample_property', None),
                createdAt=kwargs.get('createdAt', None),
                
            )
            # sample_model = SampleModel(kwargs)
            db.session.add(sample_model)
            cls.commit()  

        except SQLAlchemyError as e:
            print(f"Ha ocurrido un error de SQLAlchemy: {str(e)}")
            return None
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {str(e)}")
            return None
