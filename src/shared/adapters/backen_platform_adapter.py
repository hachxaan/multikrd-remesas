import requests
from flask import current_app
from src.shared.tools.errors.project_exception import ProjectException
from src.shared.tools.logger import internal_logger

logger = internal_logger.get_logger()


class BackendPlatformAdapter:
    def __init__(self):
        self.headers = {
            "x-api-key": current_app.config['api_key_backend_platform_out']
        }
        self.host_backend = current_app.config['host_backend_platform']

    def get_user_minimal(self, user_id: int, sms_code: str):
        url = f'{self.host_backend}/api/internal/minimal/{user_id}'

        try:
            if sms_code:
                self.headers['Sms-Code'] = sms_code

            # self.headers['second_factor_required'] = second_factor_required

            response = requests.get(url, headers=self.headers)

            # Lanza una excepción si la respuesta contiene un código de estado HTTP de 4xx o 5xx
            response.raise_for_status()

            return response.json()
        except requests.HTTPError as e:
            if response.status_code == 404:
                return response.json()
            print(str(e))
            logger.error(f'HTTP error occurred: {str(e)}')
            raise ProjectException(tag="http_error", message=str(e))
        except Exception as e:
            logger.error(f'An error occurred: {str(e)}')
            raise ProjectException(tag="unknown_error", message=str(e))
