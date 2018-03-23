from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .decorators import get_form_and_html


@get_form_and_html
def common_form(request):
    if request.method == "POST":
        #form = request.form(request.POST)
        form = request.form(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse(repr(form.cleaned_data))
    else:
        form = request.form()
    return render(request, request.html, {"form": form})
