from pathlib import Path
import os
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODELS_ROOT = os.path.join(BASE_DIR, "models/")
ROOT_URLCONF = "speechai.urls"
WSGI_APPLICATION = "speechai.wsgi.application"
ASGI_APPLICATION = "speechai.asgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

if config("CHOOSE_DB") == 1:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ["DATABASE"],
            'USER': os.environ["DB_USER"],
            'PASSWORD': os.environ["DB_PASSWORD"],
            'HOST': os.environ["DB_HOST"],
            'PORT': os.environ["DB_PORT"],
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {"format": "{levelname} {message}"},
    },
    "handlers": {
        "logfile": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/server.log",
            "maxBytes": 1000000,
            "backupCount": 3,
            "formatter": "verbose",
        },
        "console": {"level": "DEBUG", "class": "logging.StreamHandler"},
    },
    "loggers": {
        "django": {"handlers": ["logfile"], "level": "INFO", "propagate": True},
        "django.request": {
            "handlers": ["logfile"],
            "level": "INFO",
            "propagate": True,
        },
        "django.server": {"handlers": ["logfile"], "level": "INFO", "propagate": True},
    },
}

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

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ("https://192.168.192.33:1234", "https://basleshik.com.tm")


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "192.168.192.24:6379",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "example",
    }
}


CKEDITOR_UPLOAD_PATH = "posts/"
CKEDITOR_FILENAME_GENERATOR = '.utils.get_filename'
CKEDITOR_CONFIGS = CKEDITOR_CONFIGS
CKEDITOR_IMAGE_BACKEND = "pillow"

############# JAZZMIN ############
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIIN_UI_TWEAKS = JAZZMIIN_UI_TWEAKS
