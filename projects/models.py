from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    price = models.CharField(max_length=50)


    #This line below seems to cause all the problems, regardless of what the foreignkey error is
    #pricetwo = models.FloatField(max_length=4)
    
    
    
    postid = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE)

    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
 



# The old image value was this:
#   models.FilePathField(path="/img")