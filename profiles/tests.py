from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class ProfileTests(TestCase):
    """
    Tests for user registration, login, and logout.
    """

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
