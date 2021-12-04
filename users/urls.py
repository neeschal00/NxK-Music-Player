from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.contrib.auth import views as auth_views #to avoid yk
from django.contrib.auth.decorators import login_required
from users import views as user_views

def index(request):
    return HttpResponse("This is a response")

urlpatterns = [
    path('register/',user_views.registerview,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
            ),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'
            ),
        name='password_reset_confirm'),
     path('password-reset-complete/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
]
