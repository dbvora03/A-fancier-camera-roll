from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='hello_world'),
]