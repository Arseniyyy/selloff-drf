import os

from dotenv import load_dotenv


load_dotenv()

DJANGO_SECRET = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DEBUG', '') != 'False'

POSTGRES_HOST_DEV = os.environ.get('POSTGRES_HOST_DEV')
POSTGRES_NAME_DEV = os.environ.get('POSTGRES_NAME_DEV')
POSTGRES_PASSWORD_DEV = os.environ.get('POSTGRES_PASSWORD_DEV')
POSTGRES_USER_DEV = os.environ.get('POSTGRES_USER_DEV')

HOST = os.environ.get('HOST')
