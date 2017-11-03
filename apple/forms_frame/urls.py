from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'fields/multiplechoice/$', views.fields_multiplacechoice),
    url(r'fields/file/$', views.fields_file),
    url(r'fields/multiplefile/$', views.fields_multiplefile),
    url(r'fields/clearfile/$', views.fields_clearfile),
    url(r'fields/modelchoice/$', views.fields_modelchoice),
    url(r'fields/modelmultiplechoice/$', views.fields_modelmultiplechoice),

    url(r'modelforms/father/$', views.modelforms_father),
    url(r'modelforms/son/$', views.modelforms_son),

    url(r'apis/bound/$', views.apis_bound),
    url(r'apis/initial/$', views.apis_initial),
]
