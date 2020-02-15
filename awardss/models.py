from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    no_of_projects = models.IntegerField(default=0)
    #profileImage
    contact=models.CharField(max_length =30)

class ratings(models.Model):
    design
    usability
    content
