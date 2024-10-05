from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .forms import RegistrationForm, ProfileUpdateForm
from .tokens import account_activation_token
from .models import Profile


def register(request):
    """
    Handles user registration and creates a Profile with the selected role.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():

            # Save the user instance, without commit to the database yet
            user = form.save(commit=False)
            # Deactivated until email confirm
            user.is_active = False
            # Save to get the user.id
            user.save()

            # Create a profile with the role
            role = form.cleaned_data['role']
            profile = Profile.objects.create(
                user=user,
                role=role,
                email=user.email
            )

            # Send verification email
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            activation_link = reverse('activate', kwargs={
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            activation_link = f"http://{current_site.domain}{activation_link}"
            message = render_to_string('profiles/activation_email.html', {
                'user': user,
                'activation_link': activation_link,
            })

            send_mail(
                mail_subject,
                '',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                html_message=message
            )

            messages.success(
                request,
                'Please confirm your email address '
                'to complete the registration.'
            )
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'profiles/register.html', {'form': form})


def login_user(request):
    """
    Handles user login using Django's AuthenticationForm.
    """
    # Redirect logged-in users away from the login page
    if request.user.is_authenticated:
        # Redirect to the dashboard or any other page
        return redirect('dashboard')

    if request.method == "POST":
        # If the request method is POST, process the login form
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate and log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(
                        request, f'You are now logged in as {username}.')
                    return redirect('home')
                else:
                    messages.warning(
                        request,
                        'Your account is not activated. '
                        'Please check your email for the activation link.'
                    )
                    return redirect('login')
    else:
        # If the request method is GET, display an empty login form
        form = AuthenticationForm()

    return render(request, 'profiles/login.html', {'form': form})


@login_required
def logout_user(request):
    """
    Logs out the user and redirects to the homepage with a success message.
    """
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')


@login_required
def update_profile(request):
    """
    Handles updating the user's profile information, such as full name,
    email, phone, etc.
    """
    profile = request.user.profile
    # Get the user's profile instance
    if request.method == 'POST':
        # If the request method is POST, process the profile update form
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            # Save the updated profile data
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            # Redirect to the profile page after saving
            return redirect('profile')
    else:
        # If GET, prefill the form with the user's current profile data
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'profiles/profile.html', {'form': form})


@login_required
def profile_view(request):
    """
    Displays the user's profile and handles updates to profile data.
    """
    if request.method == 'POST':
        # If the request method is POST, process the profile update form
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            # Save the updated profile data
            form.save()
            messages.success(
                request, 'Your profile has been updated successfully!')
            # Redirect to the profile page after saving
            return redirect('profile')
    else:
        # GET requests, prefill the form with the user's existing profile data
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profiles/profile.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request, 'Your account has been activated! You can now log in.'
        )
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect('home')
