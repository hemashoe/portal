import os
from decouple import config
from owren.utils import EnvironmentSettings
from owren.configurations import CKEDITOR_CONFIGS, JAZZMIIN_UI_TWEAKS, JAZZMIN_SETTINGS
from owren.settings.base import (
    AUTH_PASSWORD_VALIDATORS,
    TEMPLATES,
    BASE_DIR,
)

settings_instance = EnvironmentSettings()
BASE_DIR = BASE_DIR
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles/")


ROOT_URLCONF = "owren.urls"

SECRET_KEY = settings_instance.secret_key
DEBUG = settings_instance.debug

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS_DEV", cast=lambda v: [s.strip() for s in v.split(",")]
)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    )
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "jazzmin",
    "ckeditor",
    "ckeditor_uploader",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
# CELERY

# CELERY_TIMEZONE = "Australia/Tasmania"
# CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60

# CELERY_BROKER_URL = "redis://localhost:6379"
# CELERY_RESULT_BACKEND = "redis://localhost:6379"

# CK EDITOR CONFIGS

CKEDITOR_UPLOAD_PATH = "posts/"
CKEDITOR_FILENAME_GENERATOR = "owren.configurations.get_filename"
CKEDITOR_CONFIGS = CKEDITOR_CONFIGS
CKEDITOR_IMAGE_BACKEND = "pillow"

# JAZZMIN CONFIG
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIIN_UI_TWEAKS = JAZZMIIN_UI_TWEAKS

TEMPLATES = TEMPLATES
WSGI_APPLICATION = "owren.wsgi.application"
AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS

try:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "HOST": settings_instance.database_settings["host"],
            "NAME": settings_instance.database_settings["database"],
            "USER": settings_instance.database_settings["username"],
            "PASSWORD": settings_instance.database_settings["password"],
            "PORT": settings_instance.database_settings["port"],
        }
    }
except ConnectionError:
    print("No connection")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DATETIME_FORMAT = "%Y-%m-%d %H:%M"
DATETIME_INPUT_FORMATS = "%Y-%m-%d %H:%M"
