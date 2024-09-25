from django.utils.text import slugify
from django import forms
from .models import Job


# Post a New Job form
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'excerpt', 'location']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'excerpt': forms.Textarea(attrs={'rows': 3})
        }

    # Overrides save method
    def save(self, commit=True):
        job = super().save(commit=False)
        job.status = 'open'

        # Generates unique slug
        if not job.slug:
            job.slug = self.generate_unique_slug(job.title)

        # Saves job instance
        if commit:
            job.save()
        return job

    # Generates unique slug based on title
    def generate_unique_slug(self, title):
        slug = slugify(title)
        unique_slug = slug
        num = 1

        # Checks if the slug already exists, if so, appends a number
        while Job.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug
