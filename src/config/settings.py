import os
from dotenv import load_dotenv

from src.config.constants import SALT_KEY_NAME


load_dotenv()


CONFIG = {
    'PORT': os.getenv('PUBLIC_PORT', '5000'),
    'DEBUG': os.getenv('DEBUG', 'False').lower() in ['true', '1'],
    'ROOT': os.getenv('ROOT_PATH', '/api'),

    'salt_key': (os.getenv('SECURITY_PASSWORD_SALT', 'IOwsIFSOc7RDb9oLHuZt'), os.getenv('SECRET_KEY', 'pa52eQ3OHwoAsf2W3Luh')),
    'SECURITY_PASSWORD_SALT': os.getenv('SECURITY_PASSWORD_SALT', 'IOwsIFSOc7RDb9oLHuZt'),
    'SECRET_KEY': os.getenv('SECRET_KEY', 'pa52eQ3OHwoAsf2W3Luh'),

    "logger": {
        "level": os.getenv("LOGGER_LEVEL", "INFO"),
        "disabled": os.getenv("LOGGER_DISABLED", "False"),
    },

    "solid": {
        "url": os.getenv("OPERATION_URL", "http://localhost:3002"),
        "x_api_key": os.getenv("OPERATION_X_API_KEY", "False"),
    },

    'security': {
        'X_API_KEY_RIA': os.getenv('X_API_KEY_RIA'),
        'IP_WHITE_LIST_RIA': os.getenv('IP_WHITE_LIST_RIA'),
    },

    

    'SQLALCHEMY_DATABASE_URI': f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_DNS')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}",
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'REDIS_URL': f"redis://{os.getenv('REDIS_DNS')}:{os.getenv('REDIS_PORT')}/{os.getenv('REDIS_DATABASE')}",
    'REDIS_DNS': os.getenv('REDIS_DNS'),
    'REDIS_PORT': os.getenv('REDIS_PORT'),
    'REDIS_DATABASE': os.getenv('REDIS_DATABASE'),
    'SESSION_TYPE': 'redis',
    'PERMANENT_SESSION_LIFETIME': 600,  # 10 minutes in seconds
    'MAIL_SERVER': os.getenv('MAIL_SERVER'),
    'MAIL_PORT': os.getenv('MAIL_PORT'),
    'MAIL_USE_TLS': os.getenv('MAIL_USE_TLS'),
    'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD'),
    'api_key_backend_platform_out': os.getenv('API_KEY_BACKEND_PLATFORM_OUT', 'BAf3F1dF98b20be4f4fcaB59BcBc8e54D1f9Beb1cD109FcF2a02E13b1Ce9dAF3'),
    'host_backend_platform': os.getenv('HOST_BACKEND_PLATFORM', 'http://10.209.97.4'),
    'white_list_ip': os.getenv('WHITE_LIST_IP', '127.0.0.1,10.209.97.4'),
}
