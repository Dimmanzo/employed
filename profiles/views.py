from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ProfileUpdateForm
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
            # Save the user
            user = form.save()
            # Get the role from the form
            role = form.cleaned_data['role']
            # Manually create a profile for the user with the role and email
            profile = Profile.objects.create(user=user, role=role, email=user.email)
            # Log the user in after registration
            login(request, user)
            messages.success(
                request, 'Registration successful! You are now logged in...')
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
                login(request, user)
                messages.success(
                    request, f'You are now logged in as {username}.')
                return redirect('home')
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
