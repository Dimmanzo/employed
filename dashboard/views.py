from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from .models import Application

# Create your views here.
@login_required
def dashboard(request):
    if request.user.profile.role == 'employer':
        user_jobs = Job.objects.filter(employer=request.user)
        return render(request, 'dashboard/dashboard-employer.html', {'user_jobs': user_jobs})
    elif request.user.profile.role == 'job_seeker':
        user_applications = Application.objects.filter(applicant=request.user)
        return render(request, 'dashboard/dashboard-jobseeker.html', {'user_applications': user_applications})