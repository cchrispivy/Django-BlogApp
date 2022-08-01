# TEMP SETTINGS FOR TROUBLESHOOTING #
from .common import *
import dj_database_url


DATABASES = {'default': dj_database_url.config(default='postgres://postgres:postgres@localhost/blogapp_db')}

ALLOWED_HOSTS = ['blogapp-ivy.herokuapp.com']

DEBUG = True


