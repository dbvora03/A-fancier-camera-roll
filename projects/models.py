from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    eightByTenPrice = models.CharField(max_length=4)
    eightByTenPrice = models.CharField(max_length=4)

    image =  models.CharField(max_length=100)




# models.FilePathField(path="/img")