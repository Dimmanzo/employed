from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from .models import Job
from .forms import JobForm


# View to display a list of jobs :D
class JobList(generic.ListView):
    model = Job
    template_name = "jobs/index.html"
    paginate_by = 9


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