import requests
from typing import Dict
from decimal import Decimal
from src.shared.tools.errors.project_exception import ProjectException

from src.shared.tools.logger import internal_logger


logger = internal_logger.get_logger()


class SolidOperation:
    """
    Wrapper Class to manage the Solid Transactions API
    """

    def __init__(self, instance):
        """
        Set instance of Solid to be reuse in the class, it's necessary to create the instance
        before use this class.
        :param instance:
        """

        self.instance = instance

        if self.instance is None:
            raise ProjectException("SOLID_NOT_CONNECTED")


    def user_direct_deposit(self, **kwargs) -> Dict:
        headers = {
            "service-key": self.instance.op_service_key
        }
        json_data = {
            "amount": "5", 
            "name": "Nombre Contacto", 
            "phone": "9876543210", 
            "email": "cpinacho@multikrd.com" 
        }

        url = self.instance.op_base_url + "send/ewa"
        try:
            response = requests.request("POST", url, headers=headers, json=json_data)
        except Exception as e:
            msg = f"Exception when calling Solid->user_direct_deposit: {e}"
            raise ProjectException(tag="SOLID_ERROR", message=msg)
        


    def user_direct_deposit(self, email: str, amount: Decimal) -> Dict:
        """
        Push a direct deposit in Solid to a user
        """

        headers = {
            "service-key": self.instance.op_service_key
        }
        json_data = {
            'email': str(email),
            'amount': str(amount)
        }

        url = self.instance.op_base_url + "send/ewa"
        try:
            response = requests.request("POST", url, headers=headers, json=json_data)
        except Exception as e:
            msg = f"Exception when calling Solid->user_direct_deposit: {e}"
            raise ProjectException(tag="SOLID_ERROR", message=msg)

        if response.status_code == 200:
            return True

        else:
            try:
                response_dict = response.json()
                logger.warning(f'user_direct_deposit(): url: {response.url} status: {response.status_code} '
                               f'reason: {response_dict.get("message")}')
                msg = response_dict.get("message")
                raise ProjectException(tag="SOLID_ERROR", message=msg)
            except ValueError:
                logger.warning(f'user_direct_deposit(): url: {response.url} response: {response.text}')
                raise ProjectException(tag="SOLID_ERROR", message=response.text)

    def get_user_account_number(self, email: str) -> Dict:
        """
        Get the user's account number from Solid
        """

        headers = {
            "service-key": self.instance.op_service_key
        }
        json_data = {
            'email': str(email)
        }

        url = self.instance.op_base_url + "account"
        try:
            response = requests.request("GET", url, headers=headers, json=json_data)
        except Exception as e:
            msg = f"Exception when calling Solid->get_user_account_number: {e}"
            raise ProjectException(tag="SOLID_ERROR", message=msg)

        if response.status_code == 200:
            response_dict = response.json()
            return response_dict
        else:
            try:
                response_dict = response.json()
                logger.warning(f'get_user_account_number(): url: {response.url} status: {response.status_code} '
                               f'reason: {response_dict.get("message")}')
                msg = response_dict.get("message")
                raise ProjectException(tag="SOLID_ERROR", message=msg)
            except ValueError:
                logger.warning(f'get_user_account_number(): url: {response.url} response: {response.text}')
                raise ProjectException(tag="SOLID_ERROR", message=response.text)
