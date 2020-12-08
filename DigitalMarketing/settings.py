"""
Django settings for DigitalMarketing project.

Generated by 'django-admin startproject' using Django 2.1.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#token expire time
TOKEN_EXPIRE_TIME = timedelta(hours=1)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aw6nmh!=^us^45@-&pw13d!(comtl(te*1qhbex5logib16pdx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["44.228.75.195","127.0.0.1","localhost","103.58.115.30","10.10.30.47","10.10.30.24","10.10.30.22","10.10.30.47","103.58.115.30","10.10.30.23"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    'dashboard',
    'endpoint',
    'api_digital_marketing'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'DigitalMarketing.urls'

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

WSGI_APPLICATION = 'DigitalMarketing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASE_ROUTERS = ['dashboard.router.CheckerRouter']  # it consists the path where your router.py file reside.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'digitalmarketingcopy19112020',
        #'NAME': 'digitalmarketing31102020',
        # 'NAME':'digitalmarketing1911020200_dev',
        'HOST': '10.10.30.49',
        'USER': 'root',
        'PASSWORD': 'veradis',
        'PORT': 3306,
    },
    'wp_db':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dtentrails',
        'HOST': '10.10.30.36',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/usr/python/DigitalMarketing/new_dashboard/old/110520/DigitalMarketing/static'


#logging

LOGGING = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "standard": {
                "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                "datefmt": "%Y-%b-%d %H:%M:%S"
            }
        },
        "handlers": {
            "null": {
                "level": "DEBUG",
                "class": "logging.NullHandler"
            },
            "logfile": {
                "level": "DEBUG",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": BASE_DIR + "/marketing_analytics_log.log",
                "maxBytes": 50000000,
                "backupCount": 5,
                "formatter": "standard"
            },
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "standard"
            }
        },
        "loggers": {
            "django": {
                "handlers": [
                    "console"
                ],
                "propagate": True,
                "level": "WARNING"
            },
            "django.db.backends": {
                "handlers": [
                    "console"
                ],
                "level": "DEBUG",
                "propagate": False
            },
            "dashboard": {
                "handlers": [
                    "console",
                    "logfile"
                ],
                "level": "DEBUG"
            },
            "api_digital_marketing": {
                "handlers": [
                    "console",
                    "logfile"
                ],
                "level": "DEBUG"
            }
        }
    }

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

MEDIA_URL = '/media/'
