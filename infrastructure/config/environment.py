import os

class EnvironmentConfig:
    DJANGO_SETTINGS_MODULE = os.getenv("DJANGO_SETTINGS_MODULE", "config.settings.dev")
