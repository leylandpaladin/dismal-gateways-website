from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Album
        fields = ('artist', 'album', 'genre', 'release_date', 'country', 'physical_type', 'description', 'price', 'label_number', 'cover_art_img', 'slug')

