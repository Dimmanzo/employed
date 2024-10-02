from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from jobs.models import Job
from profiles.models import Profile


class JobTests(TestCase):
    """
    Tests
    """

    def setUp(self):
        """
        Set up test data: users, profiles, and a job.
        """

        # Create users
        self.employer = User.objects.create_user(username='employer', password='password')
        self.job_seeker = User.objects.create_user(username='job_seeker', password='password')

        # Create profiles for roles
        Profile.objects.create(user=self.employer, role='employer')
        Profile.objects.create(user=self.job_seeker, role='job_seeker')

        # Create a job
        self.job = Job.objects.create(title="Job 1", slug="job-1", employer=self.employer)

    def test_job_list_view(self):
        """
        Test if the job list view renders correctly.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/index.html')

    def test_create_job(self):
        """
        Test if an employer can create a job.
        """
        self.client.login(username='employer', password='password')
        response = self.client.post(reverse('create_job'), {
            'title': 'New Job',
            'description': 'Job description',
            'excerpt': 'Short excerpt',
            'location': 'City',
            'job_type': 'full_time',
            'work_type': 'remote',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Job.objects.count(), 2)

    def test_apply_for_job(self):
        """
        Test if a job seeker can apply for a job.
        """
        self.client.login(username='job_seeker', password='password')
        response = self.client.post(reverse('apply_for_job', args=[self.job.slug]), {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'address': '123 Main St',
            'short_description': 'Experienced Developer',
            'last_jobs': 'Previous job',
            'cover_letter': 'I am interested',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to dashboard after application
        self.assertEqual(self.job.application_set.count(), 1)  # Ensure application was created
