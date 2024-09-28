from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobs.models import Job
from .models import Application

# Create your views here.
@login_required
def dashboard(request):
    if request.user.profile.role == 'employer':
        user_jobs = Job.objects.filter(employer=request.user)
        job_applications = Application.objects.filter(job__in=user_jobs)
        return render(request, 'dashboard/dashboard-employer.html', {
            'user_jobs': user_jobs,
            'job_applications': job_applications
            })
    elif request.user.profile.role == 'job_seeker':
        user_applications = Application.objects.filter(applicant=request.user)
        return render(request, 'dashboard/dashboard-jobseeker.html', {'user_applications': user_applications})


@login_required
def view_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    
    # Job Seekers view their own application
    if request.user == application.applicant:
        return render(request, 'dashboard/view_application.html', {'application': application})
    
    # Employers view applications for jobs they posted
    elif request.user == application.job.employer:
        return render(request, 'dashboard/view_application_employer.html', {'application': application})
    
    # Show an error, if not job seeker or the employer
    else:
        messages.error(request, "You do not have permission to view this application.")
        return redirect('dashboard')


@login_required
def view_application_employer(request, application_id):
    application = get_object_or_404(Application, id=application_id, job__employer=request.user)

    if request.method == 'POST':
        if 'accept' in request.POST:
            application.status = 'accepted'
            application.save()
            messages.success(request, f'Application from {application.applicant.username} has been accepted.')
        elif 'reject' in request.POST:
            application.status = 'rejected'
            application.save()
            messages.error(request, f'Application from {application.applicant.username} has been rejected.', extra_tags='danger')

        return redirect('view_application_employer', application_id=application.id)

    return render(request, 'dashboard/view_application_employer.html', {'application': application})