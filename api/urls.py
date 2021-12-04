from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import views
from .views import CustomUserCreate, BlackListToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#router makes sure that requests end up at the right resource dynamically
#if add/delete items in db urls will update to match
# from rest_framework import routers
#router works with viewset to dynamically route requests.you'll want router to go with viewse

# router = routers.DefaultRouter()
# router.register(r"songns", views.SongnViewSet)

#Wire up our API using automatic URL routing
#Additionally, we include login URLs for the browsable API
urlpatterns = [
    path('',views.apioverview,name='apioverview'),

    path('songs/all/',views.songView,name='all-songs'),
    path('songs/<int:pk>/',views.songDetail,name='song-detail'),
    path('playlists/',views.playlist,name='playlists'),
    path('playlists/detail/<int:pk>/',views.playlistDetail,name='playlist-detail'),
    path('playlists/create/',views.playlistCreate,name='create-playlist'),
    path('artists/',views.artists,name='all-artists'),
    path('artists/<str:name>/',views.artistDetail,name='artist-detail'),
    path('albums/<str:name>/',views.albumDetail,name='album-detail'),

    #authentication
    path('user/register/',CustomUserCreate.as_view(),name='create_user'),
    path('logout/blacklist/',BlackListToken.as_view(),name='blacklist'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api-auth/',include('rest_framework.urls'),name='rest_framework'),

]

