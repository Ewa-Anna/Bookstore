"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "bookstore"))

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
USER_POSTGRES = os.getenv("USER_POSTGRES")
PASSWORD_POSTGRES = os.getenv("PASSWORD_POSTGRES")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "book.apps.BookConfig",
    "user.apps.UserConfig",
    "cart.apps.CartConfig",
    "orders.apps.OrdersConfig",
    "filter.apps.FilterConfig",
    "wishlist.apps.WishlistConfig",
    "payment.apps.PaymentConfig",
    "coupons.apps.CouponsConfig",
    "taggit",
    "django_filters",
    "django.contrib.postgres",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
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

ROOT_URLCONF = "bookstore.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "cart.context_processors.cart",
                "book.context_processors.categories",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bookstore.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Postgres
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "bookstore",
        "USER": USER_POSTGRES,
        "PASSWORD": PASSWORD_POSTGRES,
        "HOST": "postgres_db", # for docker-compose
        # "HOST": "localhost",  # for terminal run
        "PORT": "5432",
    },
}

# Redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATIC_ROOT = BASE_DIR / "static"
GTK_FOLDER = r"C:\Program Files\GTK3-Runtime Win64\bin"
os.environ["PATH"] = GTK_FOLDER + os.pathsep + os.environ.get("PATH", "")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "user:dashboard"
LOGIN_URL = "user:login"
LOGOUT_REDIRECT_URL = "user:logout"
LOGOUT_URL = "user:logout"


# E-mails
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # for development
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # for production
EMAIL_HOST = os.getenv("SMTP")
EMAIL_HOST_USER = os.getenv("EMAIL_FROM")
EMAIL_HOST_PASSWORD = os.getenv("PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True


MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "user.authentication.EmailAuthBackend",
]

CART_SESSION_ID = "cart"

# Stripe
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_API_VERSION = "2023-10-16"
STRIPE_WEBHOOK_SECRET = os.getenv("endpoint_secret")

# Celery
# CELERY_BROKER_URL = "pyamqp://guest:guest@rabbitmq:5672//"
CELERY_BROKER_CONNECTION_MAX_RETRIES = 3
INVENIO_CELERY_BROKER_URL = "amqp://guest:guest@mq:5672//"
