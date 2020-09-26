import base64
import requests


class SpotifyAPIClient:
    """
    This class can be used to interact with Spotify API.
    """
    
    SPOTIFY_URL_TOKEN = 'https://accounts.spotify.com/api/token/'
    SPOTIFY_URL_NEW_RELEASES = 'https://api.spotify.com/v1/browse/new-releases'

    def __init__(self, client_id='', client_secret=''):
        """
        :param client_id: Spotify Client ID available from Spotify Developer Dashboard
        :type client_id: str
        :param client_secret: Spotify Client Secret
        :type client_secret: str
        """

        self.client_id = client_id
        self.client_secret = client_secret
        self.encoded = base64.b64encode(f'{self.client_id}:{self.client_secret}'.encode()).decode()

    def request_access_token(self):
        """
        Requests an access token for Spotify API.

        :returns: An access token for Spotify API
        :rtype: str

        :raises: requests.exceptions.HTTPError if the response is an HTTP error (e.g. 401 Unauthorized)
        """

        headers = {
            'Authorization': f'Basic {self.encoded}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(self.SPOTIFY_URL_TOKEN, headers=headers, data=body)
        response.raise_for_status()

        return response.json()['access_token']

    def request_new_releases(self, access_token=''):
        """
        Requests Spotify API `/v1/browse/new-releases` endpoint to create a list of new released albums.

        :param access_token: Spotify API access token
        :type access_token: str

        :returns: A list of new released albums (witt associated artists)
        :rtype: List[Dict]

        :raises: requests.exceptions.HTTPError if the response is an HTTP error (e.g. 401 Unauthorized)
        """

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        new_releases = []
        next_page = self.SPOTIFY_URL_NEW_RELEASES
        while next_page is not None:
            response = requests.get(next_page, headers=headers)
            response.raise_for_status()
                
            response_json = response.json()
            new_releases += self._parse_new_releases_response(response_json)
            next_page = response_json['albums']['next']

        return new_releases

    def _parse_new_releases_response(self, response_json):
        """
        Parse Spotify API `/v1/browse/new-releases` response.

        :param response_json: Spotify API `/v1/browse/new-releases` response
        :type response_json: Dict

        :returns: A list of new released albums
        :rtype: List[Dict]
        """

        return [
            {
                "name": album['name'],
                "album_type": album['album_type'],
                "release_date": album['release_date'],
                "artists": [artist['name'] for artist in album['artists']]
            }
            for album in response_json['albums']['items']
        ]
