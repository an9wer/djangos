from django.shortcuts import render
from django.http import HttpResponse

from ..models import Father, Son
from ..forms import (
    FatherForm, SonForm, PartFieldsForm, AllFieldsForm, ExcludeFieldsForm,
    OverrideFieldsFrom,)


def modelforms(request):
    if request.method == "POST":
        form = request.form(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = request.form()
    return render(request, "form.html", {"form": form})


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


def modelforms_partfields(request):
    if request.method == "POST":
        form = PartFieldsForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = PartFieldsForm()
    return render(request, "common_form.html", {"form": form})


def modelforms_allfields(request):
    if request.method == "POST":
        form = AllFieldsForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = AllFieldsForm()
    return render(request, "common_form.html", {"form": form})


def modelforms_excludefields(request):
    if request.method == "POST":
        form = ExcludeFieldsForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = ExcludeFieldsForm()
    return render(request, "common_form.html", {"form": form})


def modelforms_overridefields(request):
    print(request.path_info)
    if request.method == "POST":
        form = OverrideFieldsFrom(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = OverrideFieldsFrom()
    return render(request, "common_form.html", {"form": form})
