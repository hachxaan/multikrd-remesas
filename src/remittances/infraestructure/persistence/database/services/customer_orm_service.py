# src\remittances\infraestructure\persistence\database\services\customer_orm_service.py

from typing import Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError
from src.remittances.infraestructure.exceptions.CustomerNotFoundException import CustomerNotFoundException
from src.remittances.infraestructure.persistence.classes.meta_service import MetaService
from src.remittances.infraestructure.persistence.database.instance import database_instance as db
from src.remittances.infraestructure.persistence.database.models.customer import CustomerModel
from src.remittances.infraestructure.persistence.database.models.transfer import TransferModel
from src.shared.tools.errors.project_exception import ProjectException


class CustomerORMService(MetaService):
    def __init__(self):
        self.session = db.session

    def get_by_user_id(self, user_id: int) -> CustomerModel:
        try:
            filters = {'user_id': user_id}

            customer = self.session.query(CustomerModel).filter_by(
                **filters
            ).first()

        except SQLAlchemyError as e:
            print(f"Ha ocurrido un error de SQLAlchemy: {str(e)}")
            raise SQLAlchemyError
        except Exception as e:
            raise Exception
        if not customer:
            raise CustomerNotFoundException(message='CUSTOMER_NOT_FOUND')
        return customer

    def get_by_user_id_with_last_transfer(self, user_id: int) -> Tuple[CustomerModel, Optional[TransferModel]]:
        try:
         
            customer = self.get_by_user_id(user_id)

            last_transfer = None
            if customer:
                last_transfer = self.session.query(TransferModel).filter_by(
                    customer_uuid=customer.uuid
                ).order_by(TransferModel.created_at.desc()).first()

        except SQLAlchemyError as e:
            print(f"Ha ocurrido un error de SQLAlchemy: {str(e)}")
            raise SQLAlchemyError
        except Exception as e:
            raise Exception
        if not customer:
            raise CustomerNotFoundException(message='CUSTOMER_NOT_FOUND')
        return customer, last_transfer
