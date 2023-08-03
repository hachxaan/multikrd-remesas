# src\remittances\application\services\customer_service.py


from typing import Dict, Optional
from src.remittances.domain.repositories.customer_repository import ICustomerRepository
from src.remittances.infraestructure.exceptions.CustomerNotFoundException import CustomerNotFoundException
from src.shared.tools.errors.project_exception import ProjectException



class TransferServiceApplication:

    def __init__(
            self,
            ria_token: str,
            customer_repository: ICustomerRepository
        ):
        self.customer_repository = customer_repository
        self.ria_token = ria_token
        

    def create_transfer(self, **kwargs) -> Dict:
        try:
            customer = self.customer_repository.get_entity_by_token(
                ria_token=self.ria_token
            )
            customer.create_transfer(**kwargs)
            response = customer.send_transfer()

            # if response.get('statusCode') == 200:
            

            # else:

            
            
            
            return response


            
        except CustomerNotFoundException:   
            return {
                'statusCode': 404,
                'data': {
                    'message': 'Customer not found with the provided token.'
                }
            }


        except Exception as e:
            return {
                'statusCode': 500,
                'data': {
                    'message': str(e)
                }
            }
        
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
