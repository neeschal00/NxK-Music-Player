from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from . import views

urlpatterns = [
        path('',views.admin_dashboard,name='admin_dashboard'),
        path('addMusic/',views.addMusicview,name='add_music'),
        path('viewMusic/',views.viewMusicview,name='view_music'),
        path('viewUsers/',views.get_user,name='view_user'),
        path('delete/user/<int:user_id>/',views.delete_User,name='delete_user'),
        path('updateTo/Admin/<int:user_id>/',views.update_user_to_admin,name='update_admin'),
        path('updateMusic/<int:songn_id>/',views.updateSong),
        path('deleteMusic/<int:songn_id>/',views.deleteMusic)
    ]



