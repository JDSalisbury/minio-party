import os
import boto3
from botocore.client import Config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '%&*=#0vzfj!k&*ej&ct^3#!0abi5!yqeq28i%1e9dd1060=9%('

DEBUG = True
ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'storage.core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'storage.urls'

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

WSGI_APPLICATION = 'storage.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DCAPV = 'django.contrib.auth.password_validation.'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': DCAPV + 'UserAttributeSimilarityValidator',
    },
    {
        'NAME': DCAPV + 'MinimumLengthValidator',
    },
    {
        'NAME': DCAPV + 'CommonPasswordValidator',
    },
    {
        'NAME': DCAPV + 'NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


S3 = boto3.resource(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='NRY1PGXB4K5N8UK9XORC',
    aws_secret_access_key='uUQtcMEoX7phtXEkmvSX+C2wH7kHNaZHm600cUKh',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

BUCKET_NAME = 'local-test-media'

S3_BUCKET = S3.Bucket(BUCKET_NAME)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
