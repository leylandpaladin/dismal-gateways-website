from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class AlbumSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Album
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email','name']

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name
