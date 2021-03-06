"""apple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views

# 最后加上 /media/ 中文件的路由，否则会 404

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.root_view),
    url(r'^forms_frame/', include('forms_frame.urls')),
    url(r'^view_layer/', include('view_layer.urls')),
    url(r'^auth_tool/', include('auth_tool.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
