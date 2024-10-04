from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Job
from jobs.models import Application


@admin.register(Job)
class JobsAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Job model.
    This section defines how the Job model should be displayed
    and managed in the Django admin interface.
    It includes fields for search, filtering, and editing,
    as well as integration with Summernote for rich text editing.
    """
    list_display = ('title', 'employer', 'status', 'created_at')
    search_fields = ['title', 'employer__username']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Application model.
    This section defines how the Application model should be displayed
    and managed in the Django admin interface.
    It includes fields for filtering, searching,
    and managing applications, with a focus on managing job applications.
    """
    list_display = ('applicant', 'job', 'applied_at')
    search_fields = ['applicant__username', 'job__title']
    list_filter = ('applied_at',)
    date_hierarchy = 'applied_at'
