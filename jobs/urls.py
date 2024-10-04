from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.JobList.as_view(), name='home'),
    path('post_job/', views.create_job, name='create_job'),
    path('jobs/<slug:slug>', views.job_detail, name='job_detail'),
    path('jobs/apply/<slug:slug>/', views.apply_for_job, name='apply_for_job'),
    path('edit_job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('update_job/<int:job_id>/', views.update_job, name='update_job'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
