from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    """
    Job model represents the structure of job postings in the system.
    Each job is linked to an employer, and the status, job type, and work type are selected through predefined choices.
    It includes fields for title, description, location, and timestamps for when the job was created.
    """
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('closed', 'Closed'),
    )

    JOB_TYPE_CHOICES = (
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
    )

    WORK_TYPE_CHOICES = (
        ('remote', 'Remote'),
        ('on_site', 'On-site'),
        ('hybrid', 'Hybrid'),
    )

    # Fields for the Job model
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    excerpt = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')

    class Meta:
        ordering = ["-created_at"] # Default ordering by creation date (newest first)

    # String representation of the Job model for easy identification
    def __str__(self):
        return f"Employer: {self.employer.username} | Job Title: {self.title}"
