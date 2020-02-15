from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    no_of_projects = models.IntegerField(default=0)
    #profileImage
    contact=models.CharField(max_length =30)

class ratings(models.Model):
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    #project one to one

class Projects(models.Model):
    
