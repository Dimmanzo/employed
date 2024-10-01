from django.utils.text import slugify
from django import forms
from .models import Job


"""
Form for posting a new job.
This class defines the form fields and their associated widgets for creating a job post. 
It also overrides the save method to set the default status to 'open' and generate a unique slug based on the job title.
"""
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'excerpt', 'location', 'job_type', 'work_type']

        # Custom widgets for the description and excerpt fields
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'excerpt': forms.Textarea(attrs={'rows': 3})
        }

    """
    Overrides the default save method.
    Before saving, this method sets the job status to 'open' and ensures the slug is unique.
    """
    def save(self, commit=True):
        job = super().save(commit=False)
        job.status = 'open'

        # Generate a unique slug based on the job title if it doesn't already exist
        if not job.slug:
            job.slug = self.generate_unique_slug(job.title)

        # Save job instance
        if commit:
            job.save()
        return job

    """
    Generates a unique slug for a job post based on the title.
    If a job with the same slug exists, appends a number to make it unique.
    """
    def generate_unique_slug(self, title):
        slug = slugify(title)
        unique_slug = slug
        num = 1

        # Check if a job with the same slug already exists
        while Job.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug
