from rest_framework import serializers
from django.contrib.auth.models import User
from music.models import (
    Favourites,
    Songn,
    Playlist,
    PlaylistS
    )

class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','username','password')
        extra_kwargs = {'password':{'write_only':True}} #for security

    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
#like forms

class SongnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songn
        fields = (
            "song_title","artist",
            "album_title","genre",
            "album_art","audio_file",
            "released_year")


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ("playlist_name","playlist_description")


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songn
        fields = ("album_title","artist","album_art","song_title","genre","released_year")




