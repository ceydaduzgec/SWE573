"""
Django settings for sole project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "k8pmtm-1lktmj_x^axio41cyve!q*rrt3r)+b(-zw_^&qp4=ib"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# CHANGE THIS AFTER DONE

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "users.User"

# Application definition

INSTALLED_APPS = [
    # Django Apps
    "jazzmin",
    "sole.users",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third Party Apps
    "crispy_forms",
    # Local Apps
    "sole.core",
    "sole.posts",
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

ROOT_URLCONF = "sole.urls"

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

WSGI_APPLICATION = "sole.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ceyda",
        "USER": "cduzgec",
        "PASSWORD": "rbjh.ts67d8=6asdb38rf",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Istanbul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [BASE_DIR / "sole" / "static"]

# Media files
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.1/ref/settings/#media-root
MEDIA_ROOT = BASE_DIR / "sole" / "media"
# https://docs.djangoproject.com/en/3.1/ref/settings/#media-url
MEDIA_URL = "/media/"


# Auth views

LOGIN_URL = "users:login"
LOGIN_REDIRECT_URL = "posts:list"
LOGOUT_REDIRECT_URL = "posts:list"


# Crispy Forms

CRISPY_TEMPLATE_PACK = "bootstrap4"
