from django.test import TestCase
from unittest.mock import Mock, patch
from music_library.management.spotify_api_client import SpotifyAPIClient
from requests.exceptions import RequestException


class RequestAccessTokenTestCase(TestCase):
    """
    request_access_token method test case
    """

    def setUp(self):
        self.spotify_api_client = SpotifyAPIClient('client_id', 'client_secret')
        self.mock_post_patcher = patch('music_library.management.spotify_api_client.requests.post')
        self.mock_post = self.mock_post_patcher.start()

    def teardown(self):
        self.mock_post_patcher.stop()

    def test_access_token_is_returned(self):
        mocked_response = {'access_token': 'token'}
        self.mock_post.return_value.json.return_value = mocked_response

        response = self.spotify_api_client.request_access_token()

        self.assertEqual(response, mocked_response['access_token'])

    def test_exception_is_returned(self):
        self.mock_post.side_effect = RequestException()

        with self.assertRaises(RequestException):
            self.spotify_api_client.request_access_token()


class RequestNewReleasesTestCase(TestCase):
    """
    request_new_releases method test case
    """

    def setUp(self):
        self.spotify_api_client = SpotifyAPIClient('client_id', 'client_secret')
        self.mock_get_patcher = patch('music_library.management.spotify_api_client.requests.get')
        self.mock_get = self.mock_get_patcher.start()

    def teardown(self):
        self.mock_get_patcher.stop()

    def test_new_releases_are_returned(self):
        mocked_response = {
            'albums': {
                'items': [
                    {
                        'name': 'album_1',
                        'some_unused_key': 'value',
                        'release_date': '2020-09-23',
                        'album_type': 'single',
                        'artists': [
                            {
                                'name': 'artist_1',
                                'some_unused_key': 'value',
                            }
                        ]
                    },
                    {
                        'name': 'album_2',
                        'release_date': '2020-09-24',
                        'album_type': 'album',
                        'artists': [
                            {
                                'name': 'artist_2'
                            }
                        ]
                    },
                    {
                        'name': 'album_3',
                        'release_date': '2020-09-25',
                        'album_type': 'compilation',
                        'artists': [
                            {
                                'name': 'artist_1'
                            },
                            {
                                'name': 'artist_2'
                            }
                        ]
                    }
                ],
                'next': None
            }
        }
        self.mock_get.return_value.json.return_value = mocked_response

        response = self.spotify_api_client.request_new_releases()
        expected_reponse = [
            {
                'name': 'album_1',
                'release_date': '2020-09-23',
                'album_type': 'single',
                'artists': ['artist_1']
            },
            {
                'name': 'album_2',
                'release_date': '2020-09-24',
                'album_type': 'album',
                'artists': ['artist_2']
            },
            {
                'name': 'album_3',
                'release_date': '2020-09-25',
                'album_type': 'compilation',
                'artists': ['artist_1', 'artist_2']
            },
        ]
        
        for obj1, obj2 in zip(expected_reponse, response):
            self.assertDictEqual(obj1, obj2)

    def test_exception_is_returned(self):
        self.mock_get.side_effect = RequestException()

        with self.assertRaises(RequestException):
            self.spotify_api_client.request_new_releases()
