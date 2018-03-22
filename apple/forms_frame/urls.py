from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'fields/multivalue/$', views.common_form),
    url(r'fields/dynamic/$', views.common_form),
    # url(r'fields/multiplechoice/$', views.fields_multiplacechoice),
    # url(r'fields/file/$', views.fields_file),
    # url(r'fields/multiplefile/$', views.fields_multiplefile),
    # url(r'fields/clearfile/$', views.fields_clearfile),
    # url(r'fields/modelchoice/$', views.fields_modelchoice),
    # url(r'fields/modelmultiplechoice/$', views.fields_modelmultiplechoice),

    # url(r'modelforms/father/$', views.modelforms_father),
    # url(r'modelforms/son/$', views.modelforms_son),

    # url(r'apis/bound/$', views.apis_bound),
    # url(r'apis/initial/$', views.apis_initial),
    # url(r'apis/as/$', views.apis_as),

    # url(r'widgets/attrs/$', views.widgets_attrs),

    url(r'modelforms/partfields/$', views.common_form),
    url(r'modelforms/allfields/$', views.common_form),
    url(r'modelforms/excludefields/$', views.common_form),
    url(r'modelforms/overridefields/$', views.common_form),
    url(r'modelforms/restricted-inheritanceson/$', views.common_form),
    url(r'modelforms/expanded-inheritanceson/$', views.common_form),
]
