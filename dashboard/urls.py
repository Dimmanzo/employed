from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('application/view/<int:application_id>/', views.view_application, name='view_application'),
    path('application/employer/view/<int:application_id>/', views.view_application_employer, name='view_application_employer'),
    path('application/withdraw/<int:application_id>/', views.withdraw_application, name='withdraw_application'),
]