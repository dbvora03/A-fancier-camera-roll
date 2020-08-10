from django.urls import path
from . import views
from .views import HomeView, checkout, ItemDetailView


app_name = 'projects'



urlpatterns = [
    path('', HomeView.as_view(), name='hello_world'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name="product")
]