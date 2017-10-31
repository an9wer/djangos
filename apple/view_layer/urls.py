from django.conf.urls import url

from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^entry/$', views.entry),
]
