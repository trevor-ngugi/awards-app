from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    no_of_projects = models.IntegerField(default=0)
    #profileImage
    contact=models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Projects(models.Model):
    title=models.CharField(max_length =30)
    description=models.TextField()
    #project_image
    link=models.CharField(max_length =30)
    name=models.ForeignKey(Profile)

    def __str__(self):
        return self.title

class ratings(models.Model):
    project_name = models.OneToOneField(Projects,on_delete=models.CASCADE,primary_key=True,)
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    #project one to one
