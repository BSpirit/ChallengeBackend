from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from requests.exceptions import RequestException
import datetime

from music_library.models import Album, Artist
from music_library.management.spotify_api_client import SpotifyAPIClient


class Command(BaseCommand):
    help = 'Fetches artists from Spotify API (/v1/browse/new-releases endpoint)'

    def handle(self, *args, **options):
        app_config = apps.get_app_config('music_library')
        spotify_api_client = SpotifyAPIClient(
            app_config.SPOTIFY_CLIENT_ID, 
            app_config.SPOTIFY_CLIENT_SECRET
        )

        self.stdout.write('Requesting access Token')
        try:
            token = spotify_api_client.request_access_token()
        except RequestException  as e:
            raise CommandError('Could not retrieve access token: ' + str(e))

        self.stdout.write('Fetching artists')
        try:
            new_releases = spotify_api_client.request_new_releases(token)
        except RequestException  as e:
            raise CommandError('Could not retrieve new releases: ' + str(e))

        self.stdout.write('Updating database')
        with transaction.atomic():
            for album in new_releases:
                album_obj, _ = Album.objects.get_or_create(
                    name=album['name'],
                    album_type=album['album_type'],
                    release_date=album['release_date'],
                )
                for artist in album['artists']:
                    artist_obj, _ = Artist.objects.get_or_create(
                        name=artist
                    )
                    artist_obj.albums.add(album_obj)
