from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Job
from dashboard.models import Application


"""
Admin configuration for the Job model. 
This section defines how the Job model should be displayed and managed in the Django admin interface. 
It includes fields for search, filtering, and editing, as well as integration with Summernote for rich text editing.
"""
@admin.register(Job)
class JobsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'employer', 'status', 'created_at')
    search_fields = ['title', 'employer__username']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


"""
Admin configuration for the Application model.
This section defines how the Application model should be displayed and managed in the Django admin interface.
It includes fields for filtering, searching, and managing applications, with a focus on managing job applications.
"""
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'applied_at')
    search_fields = ['applicant__username', 'job__title']
    list_filter = ('applied_at',)
    date_hierarchy = 'applied_at'
