from src.shared.adapters.backen_platform_adapter import BackendPlatformAdapter
from src.shared.tools.logger import internal_logger

logger = internal_logger.get_logger()


class UserService:
    def __init__(self, adapter: BackendPlatformAdapter):
        self.adapter = adapter

    def get_user_minimal(self, user_id: int, sms_code: str):
        try:
            user = self.adapter.get_user_minimal(
                user_id=user_id,
                sms_code=sms_code
            )
            return user
        except Exception as e:
            logger.error(f'An error occurred: {str(e)}')
            raise
