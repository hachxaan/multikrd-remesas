import os
from dotenv import load_dotenv


load_dotenv()


CONFIG = {
    'PORT': os.getenv('PUBLIC_PORT', '5000'),
    'DEBUG': os.getenv('DEBUG', 'False').lower() in ['true', '1'],
    'ROOT': os.getenv('ROOT_PATH', '/api'),


    'SECURITY_PASSWORD_SALT': os.getenv('SECURITY_PASSWORD_SALT', 'IOwsIFSOc7RDb9oLHuZt'),
    'SECRET_KEY': os.getenv('SECRET_KEY', 'pa52eQ3OHwoAsf2W3Luh'),


    "logger": {
        "level": os.getenv("LOGGER_LEVEL", "INFO"),
        "disabled": os.getenv("LOGGER_DISABLED", "False"),
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
    'api_key_backend_platform': os.getenv('API_KEY_BACKEND_PLATFORM', '87f24deac118e63289ca643bf24c3ae4f954a61a6c041981daa9d0982e598ead'),
    'host_backend_platform': os.getenv('HOST_BACKEND_PLATFORM', 'http://10.209.97.4'),
}
