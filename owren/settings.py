import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

from .configurations import JAZZMIIN_UI_TWEAKS, JAZZMIN_SETTINGS, CKEDITOR_CONFIGS

################ ALL DIRECTORIES ################

ROOT_URLCONF = 'owren.urls'
AUTH_USER_MODEL = 'authentication.User'

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
    # "debug_toolbar",
    'corsheaders',
    'jazzmin',
    'ckeditor',
    'ckeditor_uploader',

    'app',
    'authentication',
    'main',

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
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
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
####### CK EDITOR ########

CKEDITOR_UPLOAD_PATH="posts/"
CKEDITOR_FILENAME_GENERATOR = '.utils.get_filename'
CKEDITOR_CONFIGS = CKEDITOR_CONFIGS
CKEDITOR_IMAGE_BACKEND = "pillow"

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

######### CACHE SYSTEM ###########################

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://192.168.192.24:6379",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         },
#         "KEY_PREFIX": "example"
#     }
# }

# CACHE_TTL = 60 * 30

############# LOGGING ###########################


############### LOGGING #################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "logs/voice.log",
            'maxBytes': 100000,
            'backupCount': 100,
            'formatter': 'verbose',
        },
        'console': { 
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',                                                             
        },  
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

######### DJANGO DATABASE  ############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Owren',
        'USER': 'root',
        'PASSWORD': 'P@ssw0rd',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760

############## EMAIL SERVICE ###############

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ ["EMAIL_HOST_PASSWORD"]

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