"""
WSGI config for base_project_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import environ

env = environ.Env()
ENV = env("ENV")

APPS = f"config.{ENV}"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', APPS)

application = get_wsgi_application()