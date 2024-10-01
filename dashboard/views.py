from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobs.models import Job
from .models import Application


@login_required
def dashboard(request):
    """
    Dashboard view: Displays different dashboards for employers and job seekers.
    Employers can view the jobs they posted and applications to those jobs.
    Job seekers can view their own job applications.
    """
    
    # If the user is an employer, display the employer dashboard
    if request.user.profile.role == 'employer':
        # Get jobs posted by the employer
        user_jobs = Job.objects.filter(employer=request.user)
        # Get applications for the jobs posted by the employer
        job_applications = Application.objects.filter(job__in=user_jobs)
        return render(request, 'dashboard/dashboard-employer.html', {
            'user_jobs': user_jobs,
            'job_applications': job_applications
            })
    # If the user is a job seeker, display the job seeker dashboard
    elif request.user.profile.role == 'job_seeker':
        user_applications = Application.objects.filter(applicant=request.user)
        return render(request, 'dashboard/dashboard-jobseeker.html', {'user_applications': user_applications})


@login_required
def view_application(request, application_id):
    """
    View a specific application: The logic allows both job seekers and employers to view the application.   
    Job seekers can view their own applications, while employers can view applications for the jobs they posted.
    """

    # Retrieve the specific application by its ID
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
    """
    Employers' view of applications: Allows the employer to accept or reject applications.
    Employers can view details of each application for the jobs they posted, and can take action to accept or reject applications.
    """

    # Ensure the application belongs to a job posted by the logged-in employer
    application = get_object_or_404(Application, id=application_id, job__employer=request.user)

    # If the employer submits a form to either accept or reject the application
    if request.method == 'POST':
        # If the employer accepts the application
        if 'accept' in request.POST:
            application.status = 'accepted'
            application.save()
            messages.success(request, f'Application from {application.applicant.username} has been accepted.')
        # If the employer rejects the application
        elif 'reject' in request.POST:
            application.status = 'rejected'
            application.save()
            messages.error(request, f'Application from {application.applicant.username} has been rejected.', extra_tags='danger')

        return redirect('view_application_employer', application_id=application.id)

    # Render the employer's view of the application
    return render(request, 'dashboard/view_application_employer.html', {'application': application})


@login_required
def withdraw_application(request, application_id):
    """
    Withdraw an application: Allows job seekers to withdraw their applications.
    Job seekers can confirm and withdraw an application they no longer wish to pursue.
    """

    # Ensure the application belongs to the logged-in job seeker
    application = get_object_or_404(Application, id=application_id, applicant=request.user)

    # If the job seeker submits a form to withdraw their application
    if request.method == 'POST':
        if 'withdraw' in request.POST:
            # Delete the application and show a success message
            application.delete()
            messages.success(request, "Your application has been withdrawn.")
            return redirect('dashboard')

    # Render the confirmation page for withdrawing the application
    return render(request, 'dashboard/withdraw_application.html', {'application': application})
