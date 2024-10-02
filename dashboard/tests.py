from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from dashboard.models import Application
from jobs.models import Job
from profiles.models import Profile


class DashboardTests(TestCase):
    """
    Tests for the Dashboard app, including employer and job seeker views.
    """
    def setUp(self):
        """
        Set up test data: users, profiles, jobs, and applications.
        """

        # Create users
        self.employer = User.objects.create_user(username='employer', password='password')
        self.job_seeker = User.objects.create_user(username='job_seeker', password='password')

        # Create profiles for roles
        Profile.objects.create(user=self.employer, role='employer')
        Profile.objects.create(user=self.job_seeker, role='job_seeker')

        # Create a job
        self.job = Job.objects.create(title="Job 1", slug="job-1", employer=self.employer)

        # Create an application for the job
        self.application = Application.objects.create(applicant=self.job_seeker, job=self.job, full_name="John Doe")

    def test_employer_dashboard(self):
        """
        Test if the employer dashboard renders correctly.
        """
        self.client.login(username='employer', password='password')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard-employer.html')

    def test_job_seeker_dashboard(self):
        """
        Test if the job seeker dashboard renders correctly.
        """
        self.client.login(username='job_seeker', password='password')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard-jobseeker.html')

    def test_view_application(self):
        """
        Test if the job seeker can view their application.
        """
        self.client.login(username='job_seeker', password='password')
        response = self.client.get(reverse('view_application', args=[self.application.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/view_application.html')

    def test_withdraw_application(self):
        """
        Test if the job seeker can withdraw their application.
        """
        self.client.login(username='job_seeker', password='password')
        response = self.client.post(reverse('withdraw_application', args=[self.application.id]), {'withdraw': 'true'})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Application.objects.filter(id=self.application.id).exists())
