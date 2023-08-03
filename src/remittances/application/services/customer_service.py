# src\remittances\application\services\customer_service.py


from typing import Dict, Optional
from src.remittances.domain.entities.customer import Customer
from src.remittances.domain.repositories.customer_repository import ICustomerRepository
from src.remittances.infraestructure.exceptions.CustomerNotFoundException import CustomerNotFoundException
from src.shared.services.user_service import UserService
from src.shared.tools.errors.project_exception import ProjectException



class CustomerServiceApplication:

    def __init__(
            self, 
            user_data: Dict, 
            customer_repository: ICustomerRepository,
            user_service: UserService = None
        ):
        self.customer_repository = customer_repository
        self.user_data = user_data
        self.user_service = user_service
        self.user_data['user_id'] = self.user_data.get('id')

    def createCustomer(self) -> None:

        customer = Customer.createOf(**self.user_data)
        customer.save()

    def save_token(self, token: str, ) -> None:
        try:
            customer = self.customer_repository.get_entity_by_user_id(
                user_id=self.user_data.get('id')
            )
            customer.save_token(token)
            
        except CustomerNotFoundException:
            data = self.user_service.get_user_minimal(
                user_id=self.user_data.get('id'),  
                sms_code=None
            )

            self.user_data = data.get('data')
            self.user_data['ria_token'] = token
            self.user_data['user_id'] = self.user_data.get('id')
            self.createCustomer()
            return None

        except Exception as e:
            print(type)
            raise ProjectException(f"Error: {str(e)}")       
        
    def get_by_user_id(self) -> Optional[str]:
        try:
            customer = self.customer_repository.get_entity_by_user_id(
                user_id=self.user_data.get('id')
            )
            return customer.ria_token
        except CustomerNotFoundException:
            self.createCustomer()
            return None

        except Exception as e:
            print(type)
            raise ProjectException(f"Error: {str(e)}")
