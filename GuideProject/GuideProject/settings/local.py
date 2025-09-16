from pathlib import Path
from .base import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'django-insecure-_wiaojgb&9z2d9)80tf7+wzb8(mm#pov&ywhx4mphgizi$%6d^'

DEBUG = True
ALLOWED_HOSTS = []

# Local Database - Using SQLite for easier development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
