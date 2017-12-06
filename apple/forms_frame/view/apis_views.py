from django.shortcuts import render
from django.http import HttpResponse

from ..forms import BoundForm, InitialForm, AsTableForm, AsUlForm, AsPForm


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


def apis_as(request):
    if request.method == "POST":
        table_form = AsTableForm(request.POST)
        if form.is_valid():
            return HttpResponse("ok")

        ul_form = AsUlForm(request.POST)
        if ul_form.is_valid():
            return HttpResponse("ok")

        p_form = AsPForm(request.POST)
        if p_form.is_valid():
            return HttpResponse("ok")

    else:
        table_form = AsTableForm()
        ul_form = AsUlForm
        p_form = AsPForm()
    return render(request, "apis/as.html", {"table_form": table_form,
                                            "ul_form": ul_form,
                                            "p_form": p_form})
