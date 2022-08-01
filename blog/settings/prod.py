# TEMP SETTINGS FOR TROUBLESHOOTING #
from .common import *

ALLOWED_HOSTS = ['blogapp-ivy.herokuapp.com']

DEBUG = True



DATABASES = {'default': dj_database_url.config(default='postgres://blogapp_admin:test123@localhost/blogapp_db')}
