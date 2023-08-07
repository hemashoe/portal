from decouple import config
from owren.settings.base import (
    AUTH_PASSWORD_VALIDATORS,
    ROOT_URLCONF,
    TEMPLATES,
    BASE_DIR,
)

BASE_DIR = BASE_DIR
ROOT_URLCONF = ROOT_URLCONF

SECRET_KEY = config("SECRET_KEY_DEV")
DEBUG = config("DEBUG_DEV")
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS_DEV", cast=lambda v: [s.strip() for s in v.split(",")]
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'jazzmin',
    'corsheaders',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = "speechai.urls"


WSGI_APPLICATION = "speechai.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": config("DATABASE_ENGINE_DEV"),
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Ashgabat'
DATETIME_FORMAT = '%Y-%m-%d %H:%M'
DATETIME_INPUT_FORMATS = '%Y-%m-%d %H:%M'

USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'