from rest_framework import viewsets
from music_library.models import Artist, Album
from api.serializers import ArtistSerializer, AlbumSerializer
import datetime


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('id')
    serializer_class = AlbumSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by('id')
    serializer_class = ArtistSerializer
