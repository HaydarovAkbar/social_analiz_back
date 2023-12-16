from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


###################################################################
# Django security
###################################################################

DEBUG = False


# ALLOWED_HOSTS = ['pr.sport.uz', '92.63.206.242', 'localhost']
ALLOWED_HOSTS = ['*']
"""
IF YOU WANT SET CSRF_TRUSTED_ORIGINS = ["*"] THEN YOU SHOULD SET:
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
"""

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    "https://example.com"
]

###################################################################
# CORS
###################################################################

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]