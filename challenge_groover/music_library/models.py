from django.db import models


class Album(models.Model):
    ALBUM_TYPE_CHOICE = (
        ('a', 'album'),
        ('s', 'single'),
        ('c', 'compilation'),
    )

    name = models.CharField(max_length=100)
    album_type = models.CharField(choices=ALBUM_TYPE_CHOICE, default='album', max_length=100)

    def __str__(self):
        return f'Album: {self.name}'


class Artist(models.Model):
    name = models.CharField(unique=True, max_length=100)
    albums = models.ManyToManyField(Album, related_name="artists")

    def __str__(self):
        return f'Artist: {self.name}'
