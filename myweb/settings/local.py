from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mis_cursos',
        'USER': 'postgres',
        'PASSWORD': 'jesus2711',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
