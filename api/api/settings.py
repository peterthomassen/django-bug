# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'test123'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'desecapi',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'desec',
        'USER': 'desec',
        'PASSWORD': os.environ['DESECSTACK_DBAPI_PASSWORD_desec'],
        'HOST': 'dbapi',
    },
}

AUTH_USER_MODEL = 'desecapi.User'

