import os
from dotenv import load_dotenv


load_dotenv()
host = os.getenv('ADDRESS')
secret_key = os.getenv('SECRET_KEY')
password = os.getenv('PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': host,
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
