from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from music.views import CreatePlaylistView
from . import views

urlpatterns = [
    path('playlist/',views.viewPlaylist,name='playlists-user'),
    path('playlist/new/',CreatePlaylistView.as_view(),name='playlist-create'),
    path('allsongs/',views.viewAllsongs,name='all_songs'),
    path('playlist/<int:pl_id>/', views.view_and_upPl,name="individual-playlist"),
    path('playlist/add/',views.addtopl,name="add-playlist"),
    path('playlist/delete/<int:pl_id>/',views.deletePl,name="delete-pl"),
    path('playlist/delete/song/<int:pl_id>/<int:song_id>/',views.deleteFrom_pl,name="delete-from-pl"),
    path('favourites/',views.viewFavourites, name="favs"),
    path('favourites/add/',views.addtoFav,name="like"),
    path('favourites/delete/<int:song_id>/',views.deteFromFav,name="del-fav"),
    path('explore/',views.explorepage,name="explore"),
    path('explore/ByYear/<int:year>/',views.musicByYear,name="ex-decade"),
    path('artist/<str:name>/',views.artistPage,name="artist-page"),
    ]
