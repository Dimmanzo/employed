from django.db import models
from django.contrib.auth.models import User
from django.apps import apps


class Application(models.Model):
    """
    Data structure for a job application submitted by a job seeker.
    Each Application instance links an applicant
    (a User) to a specific job (Job model).

    Fields include:
    - applicant: A ForeignKey to the User model (the person applying)
    - job: A ForeignKey to the Job model (the job being applied for)
    - full_name, email, phone, address: Personal details of the applicant
    - short_description, last_jobs, cover_letter:
      Additional information provided by the applicant
    - applied_at: The timestamp when the application was submitted
    - status: The current status of the application
      (e.g., under review, accepted, rejected)
    """
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
    status = models.CharField(
        max_length=20,
        choices=APPLICATION_STATUS_CHOICES,
        default='under_review'
    )

    # String showing applicant username and job title.
    def __str__(self):
        return f"{self.applicant.username} applied to {self.job.title}"
