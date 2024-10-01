from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model that extends the built-in User model with additional user roles 
    (either employer or job seeker).
    """

    # Role choices for the user profile
    USER_ROLES = (
        ('employer', 'Employer'),
        ('job_seeker', 'Job Seeker'),
    )

    # One-to-one relationship with User model and role field
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES)

    # String representation of the profile showing the username
    def __str__(self):
        return self.user.username
