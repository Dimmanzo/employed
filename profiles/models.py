from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    USER_ROLES = (
        ('employer', 'Employer'),
        ('job_seeker', 'Job Seeker'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES)

    def __str__(self):
        return self.user.username
