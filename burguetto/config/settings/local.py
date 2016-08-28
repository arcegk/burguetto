from base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ax(!)9zbn$=^w4k2_r8b)pgctor62w5id*c)x^as0jvz^in+(2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'burguetto',
        'HOST': 'localhost',
        'PORT': 5432,
        'USER' : 'test',
        'PASSWORD' : 'test'
    }
}

STATIC_ROOT = 'staticfiles'
