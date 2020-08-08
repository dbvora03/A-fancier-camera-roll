from django.shortcuts import render
from projects.models import Project
from django.views.generic import ListView, DetailView

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)


class HomeView(ListView):
    model = projects
    template_name = "index.html"

def checkout(request):
    return render(request, "checkout-page.html")


class ItemDetailView(DetailView):
    model = Project
    template_name = "detail.html"