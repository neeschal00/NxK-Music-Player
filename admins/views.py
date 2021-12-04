from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from music.models import *
from .forms import AddMusicForm
from django.contrib import messages
from .filters import SongnFilter
from .auth import admin_only
# Create your views here.
@login_required
@admin_only
def admin_dashboard(request):
    music = Songn.objects.all()
    music_count = music.count()
    playlist = Playlist.objects.all()
    playlist_count = playlist.count()
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    context = {
        'music':music_count,
        'playlist': playlist_count,
        'user': user_count,
        'admin':admin_count
    }
    return render(request,'admins/admind.html',context)

@login_required
@admin_only
def addMusicview(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = AddMusicForm(request.POST,request.FILES)
        if form.is_valid():
            music, created = Songn.objects.get_or_create(**form.cleaned_data)
            if created:
                messages.success(request,f'The music has been successfully added')
            else:
                messages.warning(request,f'The music {music.song_title}:{music.artist} already exits.')
            return redirect('view_music')
    else:
        # form = UserCreationForm()
        form = AddMusicForm()
    return render(request,'admins/addMusic.html',{'form': form})

@login_required
@admin_only
def get_user(request):
    users_all = User.objects.all()
    users = users_all.filter(is_staff=0)
    context = {
        'users': users,
    }
    return render(request,'admins/viewuser.html',context=context)

@login_required
@admin_only
def update_user_to_admin(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request,messages.SUCCESS,"User has been successfully updated to admin")
    return redirect('admin_dashboard')

@login_required
@admin_only
def delete_User(request,user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request,messages.SUCCESS,"User has been Deleted")
    return redirect('view_user')

@login_required
@admin_only
def viewMusicview(request):
    songs = Songn.objects.all()
    myFilter = SongnFilter(request.GET, queryset=songs)
    songs = myFilter.qs
    context = {
    'songs': songs,
    'myFilter':myFilter
    }
    return render(request,'admins/viewmusic.html',context)

@login_required
@admin_only
def deleteMusic(request,songn_id):
    songs = Songn.objects.get(id= songn_id)
    songs.delete()
    return redirect('view_music')

# def updateSong(request,songn_id):
#     instance = Songn.objects.get(id=songn_id)
#     if request.method == "POST":
#         form = AddMusicForm(request.POST,request.FILES,instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect('view_music')
@admin_only
def updateSong(request, songn_id):
        obj= get_object_or_404(Songn, id=songn_id)
        form = AddMusicForm(request.POST or None, instance= obj)
        context= {'form': form}
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            messages.success(request, "You successfully updated the Music")
            context= {'form': form}

            return redirect('view_music')

        else:
            context= {'form': form,
                       'error': 'The form was not updated successfully. Please enter in a title and content'}
            return render(request,'admins/updateMusic.html' , context)




