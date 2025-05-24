from django.shortcuts import render
from .scraper import get_job_listings

# Create your views here.

def job_list(request):
    jobs = get_job_listings()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})
