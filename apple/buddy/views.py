# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .forms import NameForm, AgeForm
from .models import Age

# Create your views here.

def index(request):
    if request.method == 'POST':
        #print request.POST['name']
        age = Age.objects.first()
        form = AgeForm(request.POST, instance=age)
        print 1211111111111
        print form.__dict__
        if form.is_valid():
            #print form.instance.age
            form.save()
            #print form.instance.age
            return HttpResponse('yes')
    else:
        form = AgeForm()
        #print 222222222222
        #print form.name
    return render(request, 'index.html', {'form': form})
