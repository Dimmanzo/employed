from django.shortcuts import render
from django.views import generic
from .models import Job

# Create your views here.
class JobList(generic.ListView):
    model = Job