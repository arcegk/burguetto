from base import *

import environ
env = environ.Env() 

DEBUG = False

SECRET_KEY = env("DJANGO_SECRET_KEY")

DATABASES = { 'default' : env.db("DATABASE_URL") } 

STATIC_ROOT = 'staticfiles'


ALLOWED_HOSTS = ['*']