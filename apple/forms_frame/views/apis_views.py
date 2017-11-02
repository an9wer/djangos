from django.shortcuts import render
from django.http import HttpResponse

from ..forms import BoundForm, InitialForm


def apis_bound(request):
    if request.method == "POST":
        form = BoundForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = BoundForm({"field_bound": "bound field"})
        print(form.is_bound)        # True
    return render(request, "apis/bound.html", {"form": form})


def apis_initial(request):
    if request.method == "POST":
        form = InitialForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = InitialForm(initial={"field": "somewords"})
    return render(request, "apis/initial.html", {"form": form})
