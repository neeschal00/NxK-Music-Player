from django.shortcuts import render
from django.http import JsonResponse


from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (SongnSerializer,
                        PlaylistSerializer,
                        AlbumSerializer,
                        RegisterUserSerializer)

from music.models import Songn, Playlist


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BlackListToken(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)




#ModelViewSet special view for rest framework that handles get and POST request
class SongnViewSet(viewsets.ModelViewSet):
    queryset = Songn.objects.all().order_by("song_title")
    serializer_class = SongnSerializer

@api_view(['GET'])
def songView(request):
    songs = Songn.objects.all().order_by("song_title")
    serializer = SongnSerializer(songs,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def songDetail(request,pk):
    song = Songn.objects.get(id=pk)
    serializer = SongnSerializer(song,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def apioverview(request):

    api_urls = {
    'Songs': 'songs/all/',
    'Playlists': '/playlists/all/',
    'Playlist Info': '/playlists/detail/<int:pk>/',
    'Create Playlist': '/playlists/create/',
    'Artists': '/artists/',
    'Artist Info': '/artsits/<str:name>',
    'Albums': '/albums/',
    'Album Info': '/albums/<str:albumn>'
    }

    return Response(api_urls)

@api_view(['GET'])
def playlist(request):
    playlists = Playlist.objects.all()
    serializer = PlaylistSerializer(playlists,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def playlistDetail(request,pk):
    playlist_data = Playlist.objects.get(id=pk)
    serializer = PlaylistSerializer(playlist_data,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def playlistCreate(request):
    serializer = PlaylistSerializer(data=request.data)
    if serializer.is_valid():

        pl, created = Playlist.objects.get_or_create(creator=request.user,**serializer.data)
        if created:
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response("Can't Create the playlist as it has already been created")
    return Response(serializer.data)


'''
def createPlaylist(request):
    serializer = PlaylistSerializer(data=request.data)

    if serializer.is_valid():
        try:
            Playlist.objects.get(playlist_name=serializer.cleaned_data["playlist_name"],creator=request.user)
            messages.warning(request,f'The playlist name already exists create new')
        except:
            pl, created = Playlist.objects.get_or_create(creator=request.user,**form.cleaned_data)
            if created:
                messages.success(request,f'The playlist has been successfully created')
            else:
                messages.warning(request,f'The music {pl.playlist_name} has already been created by')
'''
@api_view(['GET'])
def artists(request):
    music = Songn.objects.order_by('artist').values('artist').distinct()
    print(type(music))
    return Response(music)


@api_view(['GET'])
def artistDetail(request,name):
    music = Songn.objects.filter(artist=name)
    serializer = SongnSerializer(music,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def albumDetail(request,name):
    music = Songn.objects.filter(album_title=name)
    serializer = AlbumSerializer(music,many=True)
    return Response(serializer.data)


