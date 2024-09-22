from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobList.as_view(), name='home'),
]