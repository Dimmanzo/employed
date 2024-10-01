from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """
    Custom registration form that extends UserCreationForm.
    It includes an additional 'role' field to distinguish between job seekers and employers.
    """

    # Role choices for user registration
    ROLE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer'),
    )

    # Add role choice field to the form
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    # Meta class to define the model and fields for the form
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
