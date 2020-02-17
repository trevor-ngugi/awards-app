from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


#  write urls
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)