from django.urls import path
from . import views


urlpatterns = [
    path('', views.JobList.as_view(), name='home'),
    path('post_job/', views.create_job, name='create_job'),
    path('jobs/<slug:slug>', views.job_detail, name='job_detail'),
]
