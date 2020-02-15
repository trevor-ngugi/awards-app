from django.conf.urls import url
from . import views

#  write urls
urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
]