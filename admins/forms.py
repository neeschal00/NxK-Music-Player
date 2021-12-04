from django import forms
from music.models import Songn
# import datetime



class AddMusicForm(forms.ModelForm):
    class Meta:
        model = Songn
        fields = [
            'song_title',
            'artist',
            'album_title',
            'genre',
            'album_art',
            'released_year',
            'audio_file'
        ]





