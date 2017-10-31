from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'fields/multiplechoice/$', views.fields_multiplacechoice),
    url(r'fields/file/$', views.fields_file),
    url(r'fields/multiplefile/$', views.fields_multiplefile),
]
