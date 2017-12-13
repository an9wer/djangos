import os

from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

from . import views


urlpatterns = [
    url(r'built_in/400/$', views.error_400),
    url(r'built_in/403/$', views.error_403),
    url(r'built_in/404/$', views.error_404),
    url(r'built_in/500/$', views.error_500),

    url(r'request_obj/$', views.request_obj),

    url(r'serve/(?P<path>.*)$', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'view_layer', 'serve_dir'),
        'show_indexes': True,
    }),
]

"""
关于 serve(request, path, document_root=None, show_indexes=False):

The serve() view can be used to serve any directory you give it. (This view is
not hardened for production use and should be used only as a development aid;
you should serve these files in production using a real front-end web server).

Seting `show_indexes` to `True` if you'd like to serve a basic index of the
directory.

注意：django.conf.urls.static.static 本质是调用 django.views.static.serve，但
    二者的不同在于，django.conf.urls.static.static 只有在 DEBUG = True 的情况下
    才生效，而 django.views.static.serve 在 DEBUG = True 和 DEBUG = False 的
    情况下都生效。

"""


"""
Customizing error views

The default error views in Django should suffice for most Web applications, but
can easily be overridden if you need any custom behavior. Simply specify the
handlers as seen below in your URLconf (setting them anywhere else will have
no effect).

-   The page_not_found() view is overridden by handler404:

        handler404 = 'mysite.views.my_custom_page_not_found_view'

-   The server_error() view is overridden by handler500:

        handler500 = 'mysite.views.my_custom_error_view'

-   The permission_denied() view is overridden by handler403:

        handler403 = 'mysite.views.my_custom_permission_denied_view'

-   The bad_request() view is overridden by handler400:

        handler400 = 'mysite.views.my_custom_bad_request_view'

"""
