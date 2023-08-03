# src\remittances\infraestructure\persistence\database\services\customer_orm_service.py

from typing import Dict, Optional, Tuple
from sqlalchemy.exc import SQLAlchemyError
from src.remittances.infraestructure.exceptions.CustomerNotFoundException import CustomerNotFoundException
from src.remittances.infraestructure.persistence.classes.meta_service import MetaService
from src.remittances.infraestructure.persistence.database.instance import database_instance as db
from src.remittances.infraestructure.persistence.database.models.customer import CustomerModel
from src.remittances.infraestructure.persistence.database.models.transfer import TransferModel
from src.shared.ddd.domain.model.Id import Id
from src.shared.tools.errors.project_exception import ProjectException




class TransferORMService(MetaService):
    def __init__(self):
        self.session = db.session

    # def update_customer_token(self, customer_data: Dict) -> None:
    #     filters = {'user_id': customer_data.get('user_id')}
    #     customerModel = CustomerModel.query.filter_by(**filters).first()
    #     if customerModel:
    #         setattr(customerModel, 'ria_token',
    #                 customer_data.get('ria_token'))
    #         db.session.add(customerModel)
    #         db.session.commit()    
    
    def save_transfer(self, transfer_data: Dict):
        
        transferModel = TransferModel(**transfer_data)

        try:
            if transferModel:
                self.session.add(transferModel)

            self.session.commit()
        except Exception as e:
            print(type(e))
            raise e
        
    def update_transfer(self, transfer_data: Dict) -> None:
        filters = {'uuid': str(transfer_data.get('uuid').value) }
        transferModel = TransferModel.query.filter_by(**filters).first()
        if transferModel:
            for key, value in transfer_data.items():
                if hasattr(transferModel, key) and key != 'id' and key != 'uuid' and key != 'customerId':
                    setattr(transferModel, key, value)
            db.session.add(transferModel)
            db.session.commit()    
    


    # def get_by_user_id(self, user_id: int) -> CustomerModel:
    #     try:
    #         filters = {'user_id': user_id}

    #         customer = self.session.query(CustomerModel).filter_by(
    #             **filters
    #         ).first()

    #     except SQLAlchemyError as e:
    #         print(f"Ha ocurrido un error de SQLAlchemy: {str(e)}")
    #         raise SQLAlchemyError
    #     except Exception as e:
    #         raise Exception
    #     if not customer:
    #         raise CustomerNotFoundException(message='CUSTOMER_NOT_FOUND')
    #     return customer

    # def get_by_user_id_with_last_transfer(self, user_id: int) -> Tuple[CustomerModel, Optional[TransferModel]]:
    #     try:
         
    #         customer = self.get_by_user_id(user_id)

    #         last_transfer = None
    #         if customer:
    #             last_transfer = self.session.query(TransferModel).filter_by(
    #                 customer_uuid=customer.uuid
    #             ).order_by(TransferModel.created_at.desc()).first()

    #     except SQLAlchemyError as e:
    #         print(f"Ha ocurrido un error de SQLAlchemy: {str(e)}")
    #         raise SQLAlchemyError
    #     except Exception as e:
    #         raise Exception
    #     if not customer:
    #         raise CustomerNotFoundException(message='CUSTOMER_NOT_FOUND')
    #     return customer, last_transfer
