# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from view_layer.models import Entry

# Create your views here.

def entry(request):
    if request.method == "POST":
        entry = Entry(attachment=request.FILES['file_name'])
        entry.save()
        return HttpResponse('nice')
    return render(request, "entry.html")

