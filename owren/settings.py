"""
Settings for Owren project.

"""
import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

from .configurations import JAZZMIIN_UI_TWEAKS, JAZZMIN_SETTINGS

ROOT_URLCONF = 'owren.urls'
AUTH_USER_MODEL = 'authentication.User'

################ ALL DIRECTORIES ################
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')


load_dotenv(find_dotenv())
SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = True
ALLOWED_HOSTS = ["192.168.192.24", "localhost", '127.0.0.1']


########## DJANGO APPLICATIONS ###########
INSTALLED_APPS = [
    "debug_toolbar",
    'corsheaders',
    'jazzmin',
    'ckeditor',
    # 'django_forest',

    'authentication',
    'app',

    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
]

############ MIDDLEWARES AND OTHERS ################


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    "192.168.192.24",
    "127.0.0.1",
]

# FOREST = {
#    'FOREST_URL': 'https://api.forestadmin.com',
#    'FOREST_ENV_SECRET': 'c899df12612120ba8647bf09e483a8771d80eb7ee663843d6825a7b3620e5acf',
#    'FOREST_AUTH_SECRET': '936a96e338bb7c4a7695c6b8271f5ba7c37f954edf287062'
# }
# APPEND_SLASH=False

############# JAZZMIN ############
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIIN_UI_TWEAKS = JAZZMIIN_UI_TWEAKS

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

WSGI_APPLICATION = 'owren.wsgi.application'
ASGI_APPLICATION = 'owren.asgi.application'

#########   DJANGO_CORS_HEADERS ########

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-csrf-token',
    'cip',
    'isajaxrequest',
)

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]   

######### CACHE SYSTEM ###########################

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.192.24:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "example"
    }
}

CACHE_TTL = 60 * 30

######### DJANGO DATABASE  ############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'P@ssw0rd',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760

############ PASSWORD VALIDATION ###########

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

#################### INTERNALIZATION, TIMING ############################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ashgabat'
DATETIME_FORMAT=  '%Y-%m-%d %H:%M'
DATETIME_INPUT_FORMATS=  '%Y-%m-%d %H:%M'

USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

################################################################################################################