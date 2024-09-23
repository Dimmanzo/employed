from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jobs.models import Job

# Create your views here.
@login_required
def dashboard(request):
    # Filter job posts for the employer.abs
    user_jobs = Job.objects.filter(employer=request.user)
    return render(request, 'dashboard/dashboard.html', {'user_jobs': user_jobs})