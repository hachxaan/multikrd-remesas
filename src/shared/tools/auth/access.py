from functools import wraps
from typing import Callable, Dict
from flask import request


from src.config.constants import SMS_CODE_HEADER_NAME
from src.shared.adapters.backen_platform_adapter import BackendPlatformAdapter
from src.shared.cache.whitelist import WhiteList
from src.shared.services.user_service import UserService

from src.shared.tools.errors.project_exception import ProjectException
from src.shared.tools.logger import internal_logger

logger = internal_logger.get_logger()


def access_level(
    admin_company: bool = False,
    admin_peo: bool = False,
    admin_api: bool = False,
    admin_multikrd: bool = True,
    admin_multikrd_2: bool = False,
) -> Callable:
    """
    Access level wrapper to use un blueprints to manage the access level of a user in an endpoint.
    :param admin_company:
    :param admin_peo:
    :param admin_api:
    :param admin_multikrd:
    :param admin_multikrd_2:
    :return:
    """

    def check_access_level(func: Callable) -> Callable:
        @wraps(func)
        @login_required()
        def wrapper(user: Dict, *args, **kwargs) -> Callable:
            if not can_access(
                admin_company=admin_company,
                admin_peo=admin_peo,
                admin_api=admin_api,
                admin_multikrd=admin_multikrd,
                admin_multikrd_2=admin_multikrd_2,
                user=user,
            ):
                raise ProjectException("FORBIDDEN")

            return func(user, *args, **kwargs)

        return wrapper

    return check_access_level


def login_required(
    user_info: bool = False, second_factor_required: bool = False
) -> Callable:
    """
    Return the user of the token if a token exists and the decoded token is valid
    :param user_info:
    :param second_factor_required:
    :return:
    """

    def login_required_callable(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            token = request.headers.get("Authorization")

            if token is None or not is_user_logged(token=token):
                raise ProjectException(tag="NOT_AUTH")
            user_info_token = decode_from_token(token=token)

            if user_info or second_factor_required:

                backend_adapter = BackendPlatformAdapter()
                user_service = UserService(backend_adapter)
                sms_code = request.headers.get(SMS_CODE_HEADER_NAME, None)
                user_response = user_service.get_user_minimal(
                    user_id=user_info_token["id"],
                    sms_code=sms_code
                )

                if second_factor_required:
                    if SMS_CODE_HEADER_NAME not in request.headers:
                        raise ProjectException(tag="SMS_CODE_NEEDED")

                    code = user_response.get('code')
                    data = user_response.get('data')
                    if code != 200:
                        if code == 404:
                            raise ProjectException(
                                tag='VERIFICATION_SMS_NOT_FOUND')
                        else:
                            raise ProjectException(tag=user_response.get(
                                'tag'), message=user_response.get('message'))
                    elif code == 200:
                        if data:
                            if not data.get('is_sms_code_valid'):
                                raise ProjectException(tag="INVALID_CODE")
                        else:
                            raise ProjectException(
                                tag="SMS_CODE_NOT_YET_VERIFIED")

                if user_info:
                    return func(user_response, *args, **kwargs)
            else:
                return func({'data': {'id': user_info_token["id"]}}, *args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return login_required_callable


def api_key(
    user_info: str = 'platform'
) -> Callable:
    """
    Validate Api Key
    """

    def api_key_callable(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Callable:
            user_id = request.view_args.get('user_id')

            token = request.headers.get("x-api-key")

            if token is None or not is_user_logged(token=token):
                raise ProjectException(tag="NOT_AUTH")
            user_info_token = decode_from_token(token=token)

            if user_info or second_factor_required:

                backend_adapter = BackendPlatformAdapter()
                user_service = UserService(backend_adapter)
                sms_code = request.headers.get(SMS_CODE_HEADER_NAME, None)
                user_response = user_service.get_user_minimal(
                    user_id=user_info_token["id"],
                    sms_code=sms_code
                )

                if second_factor_required:
                    if SMS_CODE_HEADER_NAME not in request.headers:
                        raise ProjectException(tag="SMS_CODE_NEEDED")

                    code = user_response.get('code')
                    data = user_response.get('data')
                    if code != 200:
                        if code == 404:
                            raise ProjectException(
                                tag='VERIFICATION_SMS_NOT_FOUND')
                        else:
                            raise ProjectException(tag=user_response.get(
                                'tag'), message=user_response.get('message'))
                    elif code == 200:
                        if data:
                            if not data.get('is_sms_code_valid'):
                                raise ProjectException(tag="INVALID_CODE")
                        else:
                            raise ProjectException(
                                tag="SMS_CODE_NOT_YET_VERIFIED")

                if user_info:
                    return func(user_response, *args, **kwargs)
            else:
                return func({'data': {'id': user_info_token["id"]}}, *args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return api_key


def can_access(
    admin_company: bool,
    admin_peo: bool,
    admin_api: bool,
    admin_multikrd: bool,
    admin_multikrd_2: bool,
    user: Dict,
) -> bool:
    """
    Returns if a user can access or not depending of his access lvl
    permissions.
    :param admin_company:
    :param admin_peo:
    :param admin_api:
    :param admin_multikrd:
    :param admin_multikrd_2:
    :param usr:
    :return bool:
    """

    return (
        admin_company
        and user.admin_company
        or admin_multikrd
        and user.admin_multikrd
        or admin_peo
        and user.admin_peo
        or admin_api
        and user.admin_api
        or admin_multikrd_2
        and user.admin_multikrd_2
    )


def is_user_logged(token) -> bool:
    """
    Check if user is logged
    :param token:
    :return bool:
    """
    return token in WhiteList()


def decode_from_token(token: str) -> Dict:
    """
    Return the decoded info in the token
    :param token:
    :return Dict:
    """
    return WhiteList.decode(token=token)[0]
