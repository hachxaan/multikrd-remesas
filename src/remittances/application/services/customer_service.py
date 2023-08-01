# src\remittances\application\services\customer_service.py


from typing import Dict, Optional
from src.remittances.domain.entities.customer import Customer
from src.remittances.domain.repositories.customer_repository import ICustomerRepository
from src.remittances.infraestructure.exceptions.CustomerNotFoundException import CustomerNotFoundException
from src.shared.tools.errors.project_exception import ProjectException



class CustomerServiceApplication:

    def __init__(self, user_data: Dict, customer_repository: ICustomerRepository):
        self.customer_repository = customer_repository
        self.user_data = user_data

    def createCustomer(self) -> None:
        Customer.createOf(**self.user_data)
        
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
