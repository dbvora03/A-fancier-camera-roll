from django.shortcuts import render
from projects.models import Project
from django.views.generic import ListView, DetailView

# Create your views here.


class HomeView(ListView):
    model = Project
    template_name = "index.html"

def checkout(request):
    return render(request, "checkout-page.html")
 
class ItemDetailView(DetailView):
    model = Project
    template_name = "product.html"

"""
def detail(request):
    broject = Project.objects.get(pk=postid)
    return render(request, "product.html", {'Project': broject})
    """