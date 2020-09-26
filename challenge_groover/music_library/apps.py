from django.apps import AppConfig
from common.util import get_env_or_exception


class MusicLibraryConfig(AppConfig):
    name = 'music_library'
    SPOTIFY_CLIENT_ID = get_env_or_exception('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = get_env_or_exception('SPOTIFY_CLIENT_SECRET')
