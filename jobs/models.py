from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('pending', 'Pending'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Employer: {self.employer.username} | Job Title: {self.title}"