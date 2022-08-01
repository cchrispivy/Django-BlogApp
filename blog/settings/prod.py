# TEMP SETTINGS FOR TROUBLESHOOTING #
from .common import *

ALLOWED_HOSTS = ['blogapp-ivy.herokuapp.com']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blogapp',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}


