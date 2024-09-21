from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)