from django.shortcuts import render
from django.http import HttpResponse

from ..forms import AttrsForm


def widgets_attrs(request):
    if request.method == "POST":
        form = AttrsForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = AttrsForm()
    return render(request, "widgets/attrs.html", {"form": form})

