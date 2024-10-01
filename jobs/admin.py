from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Job
from dashboard.models import Application


# Jobs model
@admin.register(Job)
class JobsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'employer', 'status', 'created_at')
    search_fields = ['title', 'employer__username']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


# Application model
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'applied_at')
    search_fields = ['applicant__username', 'job__title']
    list_filter = ('applied_at',)
    date_hierarchy = 'applied_at'
