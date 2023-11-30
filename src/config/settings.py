from pathlib import Path
from decouple import config
from datetime import timedelta
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ['*']

# Application definition

LOCAL_APPS = [
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
]

PROD_APPS = [
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    "rest_framework_simplejwt.token_blacklist",
]

INSTALLED_APPS = LOCAL_APPS + PROD_APPS + DEV_APPS

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DATETIME_FORMAT': "%Y-%m-%d"
}

SIMPLE_JWT = {
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

gettext = lambda s: s

LANGUAGES = (
    ('uz_latn', gettext("O'zbek")),
    ('uz_cyrl', gettext('Uzbek')),
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz_latn'
MODELTRANSLATION_LANGUAGES = ('uz_latn', 'uz_cyrl', 'en', 'ru')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('uz_latn', 'uz_cyrl', 'en', 'ru')
TRANSLATABLE_MODEL_MODULES = ['app', 'organization', 'level']

MODELTRANSLATION_TRANSLATION_FILES = (
    'app.translation.translate',
    'organization.translation.translate',
    'level.translation.translate',
)

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

HOST = 'https://akbarshox.uz'

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = [HOST]

"""JAZZMIN SETTINGS"""
JAZZMIN_SETTINGS = {
    "site_title": "TTS Project Admins",
    "site_header": "TTS",
    "welcome_sign": "Welcome to TTS",
    "search_model": "auth.User",
    "user_avatar_diameter": 60,
    "user_menu": [
        {"name": "Profile", "url": "admin:auth_user_change", "icon": "user", "permissions": ["auth.change_user"]},
        {"name": "API Docs", "url": "schema-swagger-ui", "icon": "book", "permissions": ["auth.change_user"]},
        {"name": "Support", "url": " ", "icon": "question-circle", "permissions": ["auth.change_user"]},

        {"name": "Settings", "url": "admin:core_setting_changelist", "icon": "cog",
         "permissions": ["auth.change_user"]},
        {"name": "Log Out", "url": "admin:logout", "icon": "sign-out-alt"},
    ],
    "user_menu_links": [
        {"name": "TTS", "url": "https://TTS.uz", "icon": "link"},

    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "core": "fas fa-cogs",
        "HomePage": "fas fa-home",
        "sites": "fas fa-satellite",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "custom_css": None,
    "custom_js": None,

    "fieldsets": [
        ("General Information", {"fields": ["name", "logo", "favicon"]}),
        ("SEO Information", {"fields": ["site_title", "site_header", "welcome_sign"]}),
        ("Menu Options", {"fields": ["related_modal_active", "show_ui_builder", "changeform_format"]}),
        ("User Options", {"fields": ["user_avatar", "user_avatar_diameter", "user_menu"]}),
        ("Links", {"fields": ["links"]}),
        ("Icons", {"fields": ["icons", "default_icon_parents", "default_icon_children"]}),
        ("Customization", {"fields": ["custom_css", "custom_js"]}),
    ],
    "related_modal_active": False,
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    'translations': ['app'],
    'translations_auto_reload': True,
    'navigation_expanded': True,
}
