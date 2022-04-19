from pathlib import Path
from .base import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'django-insecure-_wiaojgb&9z2d9)80tf7+wzb8(mm#pov&ywhx4mphgizi$%6d^'

DEBUG = True
ALLOWED_HOSTS = []

# Local Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbStudents',
        'USER': 'postgres',
        'PASSWORD': 'qZQf6i8cHgY74$&^SU',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
