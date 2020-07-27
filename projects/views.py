from django.shortcuts import render
from projects.models import Project

# Create your views here.
def projects(response):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(response, 'projects/index.html', context)