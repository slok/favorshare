from .base import *


SECRET_KEY = '5ev)+84(e(o-$5&)4uh3b$z4+@_)rkcpsh)htcw$m5=lza4o3e'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "favorshare",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
