from django.http import Http404
from django.core.exceptions import PermissionDenied, SuspiciousOperation


def error_400(request):
    raise SuspiciousOperation

"""
django.views.defaults.bad_request(request, exception, template_name='400.html')

When a `SuspiciousOperation` is raised in Django, it may be handled by a component
of Django (for example resetting the session data). If not specifically handled,
Django will consider the current request a ‘bad request’ instead of a server error.

django.views.defaults.bad_request, is otherwise very similar to the server_error
view, but returns with the status code 400 indicating that the error condition
was the result of a client operation. By default, nothing related to the exception
that triggered the view is passed to the template context, as the exception message
might contain sensitive information like filesystem paths.

注意：django.views.defaults.bad_request 只有在 DEBUG 为 False 的情况下才会触发。

注意：django.views.defaults.bad_request 默认会去 root template directory 寻找
    名为 400.html 的页面，然后 render。如果没有找到，则使用默认的文字信息。

"""


def error_403(request):
    raise PermissionDenied

"""
django.views.defaults.permission_denied(request, exception, template_name='403.html')

If a view results in a 403 exception then Django will, by default, call the view
django.views.defaults.permission_denied. This view loads and renders the template
403.html in your root template directory, or if this file does not exist, instead
serves the text "403 Forbidden".

django.views.defaults.permission_denied is triggered by a `PermissionDenied`
exception.

注意：django.views.defaults.permission_denied 在 DEBUG 为 True 或者 False 的
    情况下均会触发。

注意：django.views.defaults.permission_denied 默认会去 root template directory
    寻找名为 403.html 的页面，然后 render。如果没有找到，则使用默认的文字信息。

"""


def error_404(request):
    raise Http404

"""
django.views.defaults.page_not_found(request, exception, template_name='404.html')

When you raise Http404 from within a view, Django loads a special view devoted
to handling 404 errors. By default, it’s the view django.views.defaults.page_not_found(),
which either produces a very simple “Not Found” message or loads and renders the
template 404.html if you created it in your root template directory.

The default 404 view will pass two variables to the template: request_path,
which is the URL that resulted in the error, and exception, which is a useful
representation of the exception that triggered the view (e.g. containing any
message passed to a specific Http404 instance).

Three things to note about 404 views:

-   The 404 view is also called if Django doesn’t find a match after checking
    every regular expression in the URLconf.

-   The 404 view is passed a RequestContext and will have access to variables
    supplied by your template context processors (e.g. MEDIA_URL).

-   If DEBUG is set to True (in your settings module), then your 404 view will
    never be used, and your URLconf will be displayed instead, with some debug
    information.

注意：django.views.defaults.page_not_found 只有在 DEBUG 为 False 的情况下
    才会触发。

注意：django.views.defaults.page_not_found 默认会去 root template directory
    寻找名为 404.html 的页面，然后 render。如果没有找到，则使用默认的文字信息。

"""


def error_500(request):
    raise Exception

"""
django.views.defaults.server_error(request, template_name='500.html')

Similarly, Django executes special-case behavior in the case of runtime errors
in view code. If a view results in an exception, Django will, by default, call
the view django.views.defaults.server_error, which either produces a very simple
"Server Error" message or loads and renders the template 500.html if you created
it in your root template directory.

The default 500 view passes no variables to the 500.html template and is rendered
with an empty Context to lessen the chance of additional errors.

If DEBUG is set to True (in your settings module), then your 500 view will never
be used, and the traceback will be displayed instead, with some debug information.

注意：django.views.defaults.server_error 只有在 DEBUG 为 False 的情况下才会触发。

注意：django.views.defaults.server_error 默认会去 root template directory
    寻找名为 500.html 的页面，然后 render。如果没有找到，则使用默认的文字信息。

"""
