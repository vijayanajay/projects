#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    print("Setting up Django environment...")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heatmaps.settings.dev")
    print(f"Using settings module: {os.environ['DJANGO_SETTINGS_MODULE']}")
    try:
        from django.core.management import execute_from_command_line

        print("Django management commands loaded successfully")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
