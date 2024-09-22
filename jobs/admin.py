from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Job


@admin.register(Job)
class JobsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'employer', 'status', 'created_at')
    search_fields = ['title', 'employer__username']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


# Register your models here.