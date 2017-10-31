from django.shortcuts import render
from django.http import HttpResponse

from .forms import MultipleChoiceForm, FileForm, MultipleFileForm


def fields_multiplacechoice(request):
    if request.method == "POST":
        form = MultipleChoiceForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = MultipleChoiceForm()
    return render(request, "multiplechoice.html", {"form": form})


def fields_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = FileForm()
    return render(request, "file.html", {"form": form})


def fields_multiplefile(request):
    if request.method == "POST":
        form = MultipleFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = MultipleFileForm()
    return render(request, "multiplefile.html", {"form": form})
