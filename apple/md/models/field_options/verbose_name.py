# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

"""
Each field type, except for ForeignKey, ManyToManyField and OneToOneField, 
takes an optional first positional argument – a verbose name. If the verbose 
name isn’t given, Django will automatically create it using the field’s 
attribute name, converting underscores to spaces.

verbose_name will be used as form's default label.
"""

class VerboseNameFK(models.Model):
    # this will only automatically create an id field
    pass

class VerboseName(models.Model):
    # the verbose name is "person's first name"
    first_name = models.CharField("person's first name", max_length=30)
    # the verbose name is "last name"
    last_name = models.CharField(max_length=30)
    # the verbose name in  ForeignKey/ManyToManyField/OneToOneField field 
    # must be added in verbose_name keyword argument
    fk = models.ForeignKey(VerboseNameFK, verbose_name="foreign key")
