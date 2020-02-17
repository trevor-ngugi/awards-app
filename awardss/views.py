from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Projects,Profile,ratings
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer

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

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.name = current_user
            project.save()
        return redirect('welcome')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

#diplsaying you single profile
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile=Profile.objects.filter(user=current_user).all()
    return render(request,"registration/profile.html",{'profile':profile})

class ProjectList(APIView):
    def get(self, request, format=None):
        projects= Projects.objects.all()
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)
