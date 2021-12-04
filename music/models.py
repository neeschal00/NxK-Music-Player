from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime
# Create your models here.
from django.utils import timezone
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from django.urls import reverse
import pytz

# timezone.activate(pytz.timezone("Asia/Kolkata"))
# timezone.localtime(timezone.now())


YEAR_CHOICES = [(r,r) for r in range(1980, datetime.date.today().year+1)]
GENRE_CHOICES = [
("Rock","Rock"),
("HipHop","HipHop"),
("Jazz","Jazz"),
("Pop","Pop"),
("Blues","Blues"),
("Alternative","Alternative"),
("Country","Country"),
("Heavy Metal","Heavy Metal"),
("Folk","Folk"),
("Classical","Classical"),
("Soul","Soul"),
("Electronic Dance Music","Electronic Dance Music"),
("Punk Rock","Punk Rock"),
("Reggae","Reggae"),
("House","House"),
("Funk","Funk"),
("Techno","Techno"),
("Alternative Rock","Alternative Rock"),
("Indie Rock","Indie Rock"),
("Trance","Trance"),
("Ambient","Ambient"),
("New Wave","New Wave"),
("Progressive Rock","Progressive Rock"),
("Dubset","Dubset"),
("Psychedelic Rock","Psychedelic Rock"),
("Opera","Opera"),
("Instrumental","Instrumental")
]
class Songn(models.Model):
    song_title = models.CharField(max_length=250)
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100,choices=GENRE_CHOICES)
    album_art = models.ImageField(upload_to='album_art/',default='default-artwork.png')
    audio_file = models.FileField(upload_to='songs/',unique=True)
    released_year = models.IntegerField(null=True,blank=True,choices=YEAR_CHOICES)

    added_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["song_title","artist","album_title"]

    def __str__(self):
        return self.song_title


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=250)
    playlist_description = models.TextField(blank=True,null=True)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["playlist_name","creator"]

    def __str__(self):
        return self.playlist_name


class PlaylistS(models.Model):
    playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    # songn = models.ForeignKey(Songn,on_delete=models.CASCADE,default=1,unique=False)
    songn = models.ManyToManyField(Songn)
    added_dt = models.DateTimeField(auto_now_add=True)


class Favourites(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    songn = models.ForeignKey(Songn,on_delete=models.CASCADE)
    added_dt = added_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user","songn"]




