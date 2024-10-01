from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.db.models import Q
from dashboard.models import Application
from .models import Job
from .forms import JobForm


# View to display and filter jobs
class JobList(generic.ListView):
    model = Job
    template_name = "jobs/index.html"
    paginate_by = 9

# Override get_queryset method to apply filters
    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(status='open')

        # Get values from GET request
        job_type = self.request.GET.get('job_type')
        work_type = self.request.GET.get('work_type')
        location = self.request.GET.get('location')
        search_query = self.request.GET.get('search')

        # Apply filters
        if job_type:
            queryset = queryset.filter(job_type=job_type)
        if work_type:
            queryset = queryset.filter(work_type=work_type)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(excerpt__icontains=search_query)
            )

        return queryset


# View to show job details
def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, 'jobs/job_detail.html', {'job': job})


# View to handle creating a new job
@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'There was an error posting the job. Please check the form and try again.')
    else:
        form = JobForm()
    return render(request, 'jobs/create_job.html', {'form': form})


@login_required
def apply_for_job(request, slug):
    # Retrieve the job based on the slug
    job = get_object_or_404(Job, slug=slug)

    # Prevent application if the job is closed
    if job.status == 'closed':
        messages.error(request, "This job is closed and no longer accepting applications.")
        return redirect('job_detail', slug=slug)

    # Check for POST request
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        short_description = request.POST.get('short_description')
        last_jobs = request.POST.get('last_jobs')
        cover_letter = request.POST.get('cover_letter')

        # Create a new Application instance
        Application.objects.create(
            applicant=request.user,
            job=job,
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            short_description=short_description,
            last_jobs=last_jobs,
            cover_letter=cover_letter,
        )

        messages.success(request, "Application submitted successfully!")
        return redirect('dashboard')

    return render(request, 'jobs/job_detail.html', {'job': job})


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, f'The job "{job.title}" was successfully updated.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job})


@login_required
def update_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user)

    if request.method == 'POST':
        if 'open' in request.POST:
            job.status = 'open'
            job.save()
            messages.success(request, f'The job "{job.title}" has been successfully opened.')
        elif 'close' in request.POST:
            job.status = 'closed'
            job.save()
            messages.success(request, f'The job "{job.title}" has been successfully closed.')
        elif 'delete' in request.POST:
            job.delete()
            messages.success(request, f'The job "{job.title}" was successfully removed.')

        return redirect('dashboard')

    return render(request, 'jobs/update_job_status.html', {'job': job})
