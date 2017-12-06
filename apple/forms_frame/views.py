from django.shortcuts import render
from django.http import HttpResponse

from .decorators import get_form_cls


@get_form_cls
def common_form(request):
    if request.method == "POST":
        form = request.form(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = request.form()
    return render(request, "common_form.html", {"form": form})
