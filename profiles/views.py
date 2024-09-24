from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm


# Create your views here.
def profile_view(request):
    return render(request, 'profiles/profile.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in...')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'profiles/register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are now logged in as {username}.')
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'profiles/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')
