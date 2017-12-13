from django.http import JsonResponse


def request_obj(request):
    print("is_ajax:", request.is_ajax())
    return JsonResponse({"is_ajax": request.is_ajax()})


"""
is_ajax():

Returns True if the request was made via an XMLHttpRequest, by checking the
HTTP_X_REQUESTED_WITH header for the string 'XMLHttpRequest'. Most modern
JavaScript libraries send this header. If you write your own XMLHttpRequest
call (on the browser side), you’ll have to set this header manually if you
want is_ajax() to work.

If a response varies on whether or not it’s requested via AJAX and you are
using some form of caching like Django’s cache middleware, you should decorate
the view with vary_on_headers('X-Requested-With') so that the responses are
properly cached.

"""
