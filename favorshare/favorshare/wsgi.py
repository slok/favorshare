"""
WSGI config for favorshare project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os


settings_prefix = "favorshare.settings"

# Get settings
settings = {
    "staging": "staging",
    "stage": "staging",
    "samdbox": "staging",
    "production": "production",
    "prod": "production",
    "local": "local",
    "vagrant": "local",
}

env = os.environ['SYSTEM_ENV']

os.environ.setdefault("DJANGO_SETTINGS_MODULE", ".".join(
    (settings_prefix, settings.get(env, "local")))
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
