# microservices/solidkrd/src/context/infrastructure/resolvers/ServiceKeyValidation.py

from flask import current_app


def validateRIA(**kwargs) -> bool:
    
    return (
        kwargs['x_api_key'] == current_app.config['X_API_KEY_RIA']
        and is_ip_in_white_list(current_app.config['IP_WHITE_LIST_RIA'], kwargs['xRealIp'])
    )  # noqa


def is_ip_in_white_list(env_var, ip_to_check):
    white_list_ips = env_var.split(',')
    return ip_to_check in white_list_ips