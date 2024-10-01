from django.urls import path
from . import views as profile_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', profile_views.register, name='register'),
    path('login/', profile_views.login_user, name='login'),
    path('logout/', profile_views.logout_user, name='logout'),
]
