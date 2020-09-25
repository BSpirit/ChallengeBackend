from django.core.exceptions import ImproperlyConfigured
import os


def get_env_or_exception(key):
    value = os.getenv(key)
    if value is None:
        raise ImproperlyConfigured(f'{key} env variable is not set')

    return value
