from django.contrib import admin
from .models import Project, Order, OrderItem

# Register your models here.

admin.site.register(Project)
admin.site.register(Order)
admin.site.register(OrderItem)