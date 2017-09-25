# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

"""
if you don’t specify primary_key=True for any fields in your model, 
Django will automatically add an IntegerField to hold the primary key, 
so you don’t need to set primary_key=True on any of your fields unless 
you want to override the default primary-key behavior.
"""

class PrimaryKey(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

if __name__ == "__main__":
    """
    NOTE: The primary key field is read-only. If you change the value of 
    the primary key on an existing object and then save it, a new object 
    will be created alongside the old one. 
    """
    p = PrimaryKey.objects.create(name="an9wer")

    # creating same column again will raise IntegrityError
    p = PrimaryKey.objects.create(name="an9wer")

    # The primary key field is read-only. If you change the value of 
    # the primary key on an existing object and then save it, a new object 
    # will be created alongside the old one.
    p.name = "Tom"
    p.save()
    Primarykey.objects.values_list()    # return value "an9wer" and "Tom"
