from django.db import models
from django.contrib.auth.models import User
from django.apps import apps


class Application(models.Model):
    APPLICATION_STATUS_CHOICES = (
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    last_jobs = models.TextField(blank=True)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES, default='under_review')

    def __str__(self):
        return f"{self.applicant.username} applied to {self.job.title}"
