import django_filters
from django_filters import CharFilter
from music.models import *

class SongFilter(django_filters.FilterSet):
    song_name= CharFilter(field_name='song_title',lookup_expr='icontains')
    class Meta:
        model = Songn
        fields = ['song_name']



