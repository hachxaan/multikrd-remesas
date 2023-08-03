import requests
from typing import Dict
from decimal import Decimal
from src.shared.tools.errors.project_exception import ProjectException

from src.shared.tools.logger import internal_logger


logger = internal_logger.get_logger()


class SolidTransfer:
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


    def transfer_execute(self, **kwargs) -> Dict:
        headers = {
            "x-api-key": self.instance.service_key
        }
        json_data = {
            "amount": kwargs.get('amount'), 
            "name":f"{kwargs.get('firs_name')} {kwargs.get('last_name')}", 
            "phone": kwargs.get('mobile_phone'), 
            "email": kwargs.get('email')
        }

        url = self.instance.base_url + "/api/remittences/intrabank"
        try:
            response = requests.request("POST", url, headers=headers, json=json_data)
            return response.json()
        except requests.RequestException as e:
            return {
                "data": {
                    "message": "The transfer service is not available at the moment."
                },
                "statusCode": 500
            }
        except Exception as e:
            msg = f"Uncontrolled exception: {e}"
            raise {
                "data": {
                    "message": msg
                },
                "statusCode": 500
            }