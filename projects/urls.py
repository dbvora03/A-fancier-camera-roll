from django.urls import path
from . import views
from .views import HomeView, checkout, ItemDetailView



urlpatterns = [
    path('', HomeView.as_view(), name='hello_world'),
    path('checkout/', views.checkout, name='checkout'),
    #path('<slug:slug>/', ItemDetailView.as_view(), name="product")
    path('<int:pk>/', ItemDetailView.as_view(), name = 'detail')
]