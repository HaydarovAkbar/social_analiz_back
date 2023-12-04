from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = False


ALLOWED_HOSTS = ['pr.sport.uz', '92.63.206.242', 'localhost']