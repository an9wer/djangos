from django.shortcuts import render
from django.http import HttpResponse

from ..models import FileModel
from ..forms import (
    MultipleChoiceForm, FileForm, MultipleFileForm, ClearFileForm,
    ModelChoiceForm, ModelMultipleChoiceForm)


def fields_multiplacechoice(request):
    if request.method == "POST":
        form = MultipleChoiceForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = MultipleChoiceForm()
    return render(request, "fields/multiplechoice.html", {"form": form})


def fields_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = FileForm()
    return render(request, "fields/file.html", {"form": form})


def fields_multiplefile(request):
    if request.method == "POST":
        form = MultipleFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = MultipleFileForm()
    return render(request, "fields/multiplefile.html", {"form": form})


def fields_clearfile(request):
    if request.method == "POST":
        form = ClearFileForm(request.POST, request.FILES)
        print(form.is_bound)        # True
        if form.is_valid():
            file_model = FileModel(field=request.FILES.get("field"))
            file_model.save()
            return HttpResponse("ok")
    else:
        file_model = FileModel.objects.first()
        # 显示 clear checkbox
        form = ClearFileForm(initial={"field": getattr(file_model, "field", None)})
        print(form.is_bound)        # False

        """ 注意：下面的写法不会显示 clear checkbox
        form = ClearFileForm({"field": getattr(file_model, "field", None)})
        print(form.is_bound)        # True

        """
    return render(request, "fields/clearfile.html", {"form": form})


def fields_modelchoice(request):
    if request.method == "POST":
        form = ModelChoiceForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = ModelChoiceForm()
    return render(request, "fields/modelchoice.html", {"form": form})


def fields_modelmultiplechoice(request):
    if request.method == "POST":
        form = ModelMultipleChoiceForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("ok")
    else:
        form = ModelMultipleChoiceForm()
    return render(request, "fields/modelmultiplechoice.html", {"form": form})
