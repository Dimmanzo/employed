from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileTests(TestCase):
    """
    Tests for user registration, login, and logout.
    """

    def setUp(self):
        """
        Set up test data: create users and their profiles.
        """
        # Create an employer user
        self.employer_user = User.objects.create_user(
            username='employer_user', password='password'
        )
        Profile.objects.create(user=self.employer_user, role='employer')

        # Create a job seeker user
        self.job_seeker_user = User.objects.create_user(
            username='job_seeker_user', password='password'
        )
        Profile.objects.create(user=self.job_seeker_user, role='job_seeker')

    def test_register_user(self):
        """
        Test if a user can register successfully.
        """
        response = self.client.post(reverse('register'), {
            'username': 'new_user',
            'email': 'new_user@example.com',
            'password1': 'strongpassword',
            'password2': 'strongpassword',
            'role': 'job_seeker'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='new_user').exists())

    def test_login_user(self):
        """
        Test if a user can log in successfully.
        """
        user = User.objects.create_user(username='user1', password='password')
        response = self.client.post(reverse('login'), {
            'username': 'user1',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(int(self.client.session['_auth_user_id']), user.pk)

    def test_logout_user(self):
        """
        Test if a user can log out successfully.
        """
        user = User.objects.create_user(username='user1', password='password')
        self.client.login(username='user1', password='password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_profile_update(self):
        """
        Test if a user can update their profile successfully.
        """

        # Create a user and log them in
        user = User.objects.create_user(username='user2', password='password')
        self.client.login(username='user2', password='password')

        # Create profile associated with user
        profile = Profile.objects.create(
            user=user,
            full_name='John Doe',
            phone='123456789',
            bio='Developer'
        )

        # Update profile details
        response = self.client.post(reverse('profile'), {
            'full_name': 'Jane Doe',
            'phone': '987654321',
            'bio': 'Senior Developer'
        })

        # Refresh profile from the database
        profile.refresh_from_db()

        # Check if the profile is updated
        self.assertEqual(profile.full_name, 'Jane Doe')
        self.assertEqual(profile.phone, '987654321')
        self.assertEqual(profile.bio, 'Senior Developer')
        self.assertEqual(response.status_code, 302)

    def test_employer_redirection(self):
        """
        Test if an employer is redirected to the correct employer dashboard.
        """
        self.client.login(username='employer_user', password='password')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard-employer.html')

    def test_job_seeker_redirection(self):
        """
        Test if a job seeker is redirected to the correct job seeker dashboard.
        """
        self.client.login(username='job_seeker_user', password='password')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard-jobseeker.html')
