from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    """
    Job model represents the structure of job postings in the system.
    Each job is linked to an employer, and the status, job type,
    and work type are selected through predefined choices.
    It includes fields for title, description, location,
    and timestamps for when the job was created.
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
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='open'
    )

    class Meta:
        ordering = ["-created_at"]  # Ordering by creation date (newest first)

    # String representation of the Job model for easy identification
    def __str__(self):
        return f"Employer: {self.employer.username} | Job Title: {self.title}"


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
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)
    cover_letter_file = models.FileField(
        upload_to='cover_letters/', null=True, blank=True
    )
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=APPLICATION_STATUS_CHOICES,
        default='under_review'
    )

    # String showing applicant username and job title.
    def __str__(self):
        return f"{self.applicant.username} applied to {self.job.title}"
