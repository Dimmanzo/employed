from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegistrationForm(UserCreationForm):
    """
    Custom registration form that extends UserCreationForm.
    Includes 'role' field to distinguish between job seekers and employers.
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


class ProfileUpdateForm(forms.ModelForm):
    """
    Handles user profile updates by allowing users to change
    their full name, email, phone, address, and bio.
    The form is pre-filled with
    existing profile information, and when saved,
    it updates the user's profile details.
    """

    class Meta:
        # Meta class to define the model and fields for the form
        model = Profile
        fields = ['full_name', 'email', 'phone', 'address', 'bio']

    def __init__(self, *args, **kwargs):
        # Populatesg form with the user's existing profile information.
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        # Prefill Profile model fields
        self.fields['full_name'].initial = self.instance.full_name
        self.fields['email'].initial = self.instance.email

        # Add Bootstrap styling to all fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    def save(self, commit=True):
        # Saves the form data to the Profile model.
        profile = super().save(commit=False)

        # Save the Profile model fields
        profile.full_name = self.cleaned_data['full_name']
        profile.email = self.cleaned_data['email']
        if commit:
            profile.save()
        return profile
