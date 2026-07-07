"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

django_env = os.getenv("DJANGO_ENV", 'development')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"config.settings.{django_env}")

application = get_wsgi_application()
