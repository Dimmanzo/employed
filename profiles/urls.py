from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as profile_views


urlpatterns = [
    path('', profile_views.update_profile, name='profile'),
    path('register/', profile_views.register, name='register'),
    path('login/', profile_views.login_user, name='login'),
    path('logout/', profile_views.logout_user, name='logout'),
    path(
        'activate/<uidb64>/<token>/', profile_views.activate, name='activate'
    ),
]
