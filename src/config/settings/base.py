from pathlib import Path
from decouple import config
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# Application definition

LOCAL_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DEV_APPS = [
    'app',
    'organization',
    'social',
    'account',
    'level',
    'utils',
    'television',
    'bot.apps.BotConfig',
]

PROD_APPS = [
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    "rest_framework_simplejwt.token_blacklist",
    'drf_yasg',
    'axes',
    'django_filters',
    'django_celery_results',
    'django_celery_beat',
    'django_extensions',
]

INSTALLED_APPS = LOCAL_APPS + PROD_APPS + DEV_APPS

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # translate
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#### to environment variables
AUTH_USER_MODEL = "account.User"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# DRF settings

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
}

# JWT settings

SIMPLE_JWT = {
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
}

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
    # AxesStandaloneBackend should be the first backend in the
    'axes.backends.AxesStandaloneBackend',
]

# AXES settings

# AXES_LOCKOUT_URL = '/account/lockout/'
AXES_FAILURE_LIMIT = 3
AXES_LOCKOUT_PARAMETERS = ["ip_address", ["username", "user_agent"]]
AXES_COOLOFF_TIME = timedelta(minutes=1)
AXES_CACHE = 'axes'

# LOGGING settings

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'axes_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'axes.log',
        },
    },
    'loggers': {
        'axes': {
            'handlers': ['axes_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

USE_I18N = True

USE_L10N = True

gettext = lambda s: s

LANGUAGES = (
    ('oz', gettext("O'zbek")),
    ('uz', gettext('Ўзбек тили')),
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('oz', 'uz', 'en', 'ru')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('oz', 'uz', 'en', 'ru')

MODELTRANSLATION_TRANSLATION_FILES = (
    'app.translation.translate',
    'organization.translation.translate',
    'level.translation.translate',
    'utils.translation.translate',
)

TIME_ZONE = "Asia/Tashkent"

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'Accept',
    'Accept-Charset',
    'Authorization',
    'Content-Type',
    # Add any other headers needed by your Swagger setup
    'Access-Control-Allow-Origin',
    'Access-Control-Allow-Methods',
    'Access-Control-Allow-Headers',
    'Access-Control-Allow-Credentials',
]
HOST = 'https://9a9b-194-93-24-3.ngrok-free.app'

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = [HOST]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

# Celery settings

CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = "redis://localhost:6379"

CELERY_TIMEZONE = "Asia/Tashkent"

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 5 * 60
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# Bot settings
TOKEN = config("TOKEN")

# PARSING SETTINGS

TG_PARSE_MSG_COUNT = 350

LIVEDONE_TOKEN = config('LIVEDONE_TOKEN')
LIVEDONE_POST_URL = "https://api.livedune.ru/accounts/ID/posts"
LIVEDONE_ACCOUNTS_URL = "https://api.livedune.ru/accounts"


MINIO_HOST = config("MINIO_HOST")
MINIO_ACCESS_KEY = config("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = config("MINIO_SECRET_KEY")
MINIO_BUCKET_NAME = config("MINIO_BUCKET_NAME")
MINIO_SECURE = False
