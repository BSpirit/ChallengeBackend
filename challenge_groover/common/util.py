from django.core.exceptions import ImproperlyConfigured
import os


def get_env_or_exception(key):
    """
    Gets an environnement variable. Raises an exception if it doesn't exist.

    :param key: env variable key
    :type key: str

    :returns: env variable value
    :rtype: str

    :raises: django.core.exceptions.ImproperlyConfigured if env variable doesn't exist
    """
    
    value = os.getenv(key)
    if value is None:
        raise ImproperlyConfigured(f'{key} env variable is not set')

    return value
