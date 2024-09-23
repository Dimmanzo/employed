from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistrationForm
from .models import Job


# Create your views here.
class JobList(generic.ListView):
    model = Job
    template_name = "jobs/index.html"
    paginate_by = 3


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('home')
    else:
        form = RegistrationForm()
        print(form.errors)
    return render(request, 'register.html', {'form': form})