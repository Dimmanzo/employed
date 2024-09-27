from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('application/<int:application_id>/view/', views.view_application, name='view_application'),
]