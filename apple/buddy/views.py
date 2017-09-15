# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .forms import NameForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        #print request.POST['name']
        form = NameForm(request.POST)
        print 1211111111111
        print form.__dict__
        #print form.name
        if form.is_valid():
            return HttpResponse('yes')
    else:
        form = NameForm()
        #print 222222222222
        #print form.name
    return render(request, 'index.html', {'form': form})
