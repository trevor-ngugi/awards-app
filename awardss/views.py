from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Projects
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    projects=Projects.show_projects()
    return render(request, 'projects/landing.html',{'projects':projects})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects= Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'projects/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'projects/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def project(request,project_id):
    try:
        project = Projects.objects.get(id = project_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"projects/project.html", {"project":project})
