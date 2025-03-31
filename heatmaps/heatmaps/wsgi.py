"""
WSGI config for heatmaps project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import environ

from django.core.wsgi import get_wsgi_application

# Initialize environment variables
env = environ.Env()
env_file = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"
)
if os.path.isfile(env_file):
    environ.Env.read_env(env_file)

# Set the default Django settings module
django_settings = env(
    "DJANGO_SETTINGS_MODULE", default="heatmaps.settings.prod"
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings)

# Get the WSGI application
application = get_wsgi_application()
