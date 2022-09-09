from rest_framework import serializers
from .models import Album, UserItem


class AlbumSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Album
        fields = ('pk', 'artist', 'album', 'genre', 'release_date', 'country', 'physical_type', 'description', 'price', 'label_number', 'cover_art_img','stock', 'slug')

class UserItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserItem
        fields = ('item', 'user', 'quantity', 'added')

