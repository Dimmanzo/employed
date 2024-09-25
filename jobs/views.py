from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
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

        # Get values from GET request
        job_type = self.request.GET.get('job_type')
        work_type = self.request.GET.get('work_type')
        location = self.request.GET.get('location')

        # Apply filters
        if job_type:
            queryset = queryset.filter(job_type=job_type)
        if work_type:
            queryset = queryset.filter(work_type=work_type)
        if location:
            queryset = queryset.filter(location__icontains=location)

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