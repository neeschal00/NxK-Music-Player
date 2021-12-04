from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import *
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CreatePlaylistForm
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .filters import SongFilter
import json

@login_required
def viewPlaylist(request):

    userplaylist = Playlist.objects.filter(creator=request.user)
    if request.method == 'POST':
        form = CreatePlaylistForm(request.POST)
        if form.is_valid():
            try:
                Playlist.objects.get(playlist_name=form.cleaned_data["playlist_name"],creator=request.user)
                messages.warning(request,f'The playlist name already exists create new')
            except:
                pl, created = Playlist.objects.get_or_create(creator=request.user,**form.cleaned_data)
                print(form.cleaned_data)
                if created:
                    messages.success(request,f'The playlist has been successfully created')
                else:
                    messages.warning(request,f'The music {pl.playlist_name} has already been created by')
            return redirect('playlists-user')
    else:
        # form = UserCreationForm()
        form = CreatePlaylistForm()
    return render(request,'music/userplaylist.html',{'form': form,'userplaylist': userplaylist})

@login_required
def viewAllsongs(request):

    music = Songn.objects.all()
    myFilter = SongFilter(request.GET, queryset=music)
    user_pl = Playlist.objects.filter(creator=request.user)
    music = myFilter.qs
    music_count = music.count()
    favs = Favourites.objects.filter(user=request.user.id)
    favs = Songn.objects.filter(id__in = favs.values_list('songn')).values_list('id',flat=True)
    context = {
        'music':music,
        'music_count':music_count,
        'myFilter': myFilter,
        'userplaylist': user_pl,
        'favs': favs
    }
    return render(request,'music/allsongs.html',context)


class CreatePlaylistView(CreateView):
    model = Playlist
    fields = ['playlist_name','playlist_description']
    success_url = reverse_lazy('playlists-user')

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

@login_required
def view_and_upPl(request,pl_id):
    instance = get_object_or_404(Playlist,id=pl_id)

    playlist_d = Playlist.objects.get(id=pl_id)
    playlistS_inst = PlaylistS.objects.filter(playlist=playlist_d)

    music = Songn.objects.filter(id__in = playlistS_inst.values_list('songn')) #Filtering with id in for multiple item

    if request.method == "POST":
        form = CreatePlaylistForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect("individual-playlist", pl_id=pl_id)
    context = {
        'form': CreatePlaylistForm(instance=instance),
        'playlistd': playlist_d,
        'music': music
    }
    return render(request, 'music/updatePlnView.html',context)


def deletePl(request,pl_id):
    playlist_d = Playlist.objects.get(id=pl_id)
    playlist_d.delete()
    return redirect('playlists-user')

def addtopl(request):

    if request.is_ajax() and request.method == "POST":
        song_id = json.loads(request.POST.get('songId'))
        playlist_id = json.loads(request.POST.get('playlistId'))
        songn_inst = Songn.objects.get(id=song_id) #instance of song to use in get or create
        playlist_inst = Playlist.objects.get(id=playlist_id)
        try:
            data = PlaylistS.objects.get(playlist=playlist_inst,songn=songn_inst)
            return JsonResponse({
                    'msg': f"The song already exist in the playlist wit"
                    })
        except Exception as e:
            add_s = PlaylistS(playlist=playlist_inst)
            add_s.save()
            add_s.songn.add(songn_inst)

            if add_s:
                return JsonResponse({
                    'msg': f"The song is added to the playlist"
                    })





def deleteFrom_pl(request,pl_id,song_id):
    songn_inst = Songn.objects.get(id=song_id) #instance of song to use in get or create
    playlist_inst = Playlist.objects.get(id=pl_id)
    data = PlaylistS.objects.get(playlist=playlist_inst,songn=songn_inst)
    data.delete()
    return redirect('individual-playlist', pl_id=pl_id)




@login_required
def viewFavourites(request):

    music = Favourites.objects.filter(user=request.user.id)
    music = Songn.objects.filter(id__in = music.values_list('songn'))

    music_count = music.count()
    context = {
        'music':music,
        'music_count':music_count
    }
    return render(request,'music/userfavs.html',context)

@login_required
def addtoFav(request):
    user = request.user
    if request.is_ajax() and request.method == "POST":
        sentdata = json.loads(request.POST.get('songId'))

        songn_inst = Songn.objects.get(id=sentdata) #instance of song to use in get or create
        data, created = Favourites.objects.get_or_create(user=user,songn=songn_inst)
        if created:
            return JsonResponse({
                'msg': f"The song is added to favourites"
                })
        else:
            return JsonResponse({
                'msg': f"The song already exist in your favourites"
                })

@login_required
def deteFromFav(request,song_id):
    user_inst = request.user
    song_inst = Songn.objects.get(id=song_id)

    fav_data = Favourites.objects.get(user=user_inst,songn=song_inst)
    fav_data.delete()
    return redirect('favs')

@login_required
def explorepage(request):
    music = Songn.objects.order_by('added_dt')[::-1]
    distint_artist = Songn.objects.order_by('artist').values('artist').distinct()
    context = {
        'music':music,
        'artists':distint_artist
    }
    return render(request,'music/explorepage.html',context)


def musicByYear(request,year):
    limit_y = year + 10
    music= Songn.objects.filter(released_year__gte=year, released_year__lt=limit_y)
    context = {
    'music': music,
    'imageurl': f"/static/images/{year}s.jpg"
    }
    return render(request,'music/byYear.html',context)


def artistPage(request,name):
    music = Songn.objects.filter(artist=name)
    artist_name = name
    context = {
    'music': music,
    'artist': artist_name
    }
    print(music)
    return render(request,'music/artistpage.html',context)



