from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    #name = models.CharField(User,max_length=30)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length =30)
    no_of_projects = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to = 'profile/')
    contact=models.CharField(max_length =30)

    def save_profile(self):
        self.save()
    
    def __str__(self):
        return f"{self.user.username} profile"

    



class Projects(models.Model):
    title=models.CharField(max_length =30)
    description=HTMLField()   #models.TextField()
    #project_image
    project_image = models.ImageField(upload_to = 'project/')
    link=models.CharField(max_length =30)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pub_date']

    @classmethod
    def show_projects(cls):
        projects= cls.objects.order_by('pub_date')
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

class ratings(models.Model):
    project_name = models.OneToOneField(Projects,on_delete=models.CASCADE,primary_key=True,)
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    #project one to one
