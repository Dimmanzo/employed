from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Employer: {self.employer.username} | Job Title: {self.title}"