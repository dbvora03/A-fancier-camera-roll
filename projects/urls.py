from django.urls import path
from . import views
from .views import HomeView, checkout, ItemDetailView

urlpatterns = [
    path('', views.projects, name='hello_world'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/<slug>/', views.ItemDetailView, name="product")
]