from django.shortcuts import render
from django.http import HttpResponse

from ..models import Father, Son
from ..forms import FatherForm, SonForm


def modelforms_father(request):
    if request.method == "POST":
        form = FatherForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = FatherForm()
    return render(request, "modelforms/father.html", {"form": form})


def modelforms_son(request):
    if request.method == "POST":
        form = SonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("ok")
    else:
        son = Son.objects.first()
        form = SonForm(instance=son)
        print(form.is_bound)        # False
        #form= SonForm()
    return render(request, "modelforms/son.html", {"form": form})
