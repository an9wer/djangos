from django.conf.urls import url

from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='in'),
    url(r'^index/$', views.index),
]
