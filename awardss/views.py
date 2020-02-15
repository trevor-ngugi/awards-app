from django.shortcuts import render
from .models import Projects

# Create your views here.
def welcome(request):
    projects=Projects.show_projects()
    return render(request, 'projects/landing.html',{'projects':projects})
