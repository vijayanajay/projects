# heatmaps/heatmaps/settings/dev.py

from .base import *

print("Loading development settings...")

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Database configuration for development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME_DEV"),
        "USER": env("DB_USER_DEV"),
        "PASSWORD": env("DB_PASSWORD_DEV"),
        "HOST": env("DB_HOST_DEV"),
        "PORT": env("DB_PORT_DEV"),
    }
}

print(f"Database settings: {DATABASES['default']}")

# Static files configuration
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "static"
    ),
]

print(f"Static files directories: {STATICFILES_DIRS}")
print(f"Base directory: {BASE_DIR}")

# Media files configuration
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
