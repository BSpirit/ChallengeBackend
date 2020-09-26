from music_library.models import Artist, Album
from rest_framework import serializers


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    albums = serializers.HyperlinkedRelatedField(many=True, view_name='album-detail', read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'albums']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.HyperlinkedRelatedField(many=True, view_name='artist-detail', read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'name', 'album_type', 'release_date', 'artists']
