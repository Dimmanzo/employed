from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ProfileUpdateForm


def register(request):
    """
    Handles user registration. Saves the role from the registration form and logs in the user after successful registration.
    """
    # Redirect logged-in users away from the register page
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard or any other page

    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user without committing to add the role
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.save()
            # Log the user in and redirect to the homepage
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in...')
            return redirect('home')
    else:
        # If the request method is GET, display an empty registration form
        form = RegistrationForm()
    return render(request, 'profiles/register.html', {'form': form})


def login_user(request):
    """
    Handles user login using Django's AuthenticationForm.
    """
    # Redirect logged-in users away from the login page
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard or any other page
        
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
                messages.success(request, f'You are now logged in as {username}.')
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
    Handles updating the user's profile information, such as full name, email, phone, etc.
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
        # If the request method is GET, prefill the form with the user's current profile data
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
            messages.success(request, 'Your profile has been updated successfully!')
            # Redirect to the profile page after saving
            return redirect('profile')
    else:
        # For GET requests, prefill the form with the user's existing profile data
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profiles/profile.html', {'form': form})
