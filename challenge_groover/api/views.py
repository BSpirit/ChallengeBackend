from rest_framework import viewsets
from music_library.models import Artist, Album
from api.serializers import ArtistSerializer, AlbumSerializer
import datetime


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allow albums to be viewed or edited.
    """
    queryset = Album.objects.all().order_by('id')
    serializer_class = AlbumSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoints that allow artists to be viewed or edited.
    """
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer
