# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class M2M_Person(models.Model):
    name  = models.CharField(max_length=128)

class M2M_Group(models.Model):
    name = models.CharField(max_length=128)
    persons = models.ManyToManyField(M2M_Person, through="M2M_Membership",
                                     related_name='groups')

class M2M_Membership(models.Model):
    person = models.ForeignKey(M2M_Person)
    group = models.ForeignKey(M2M_Group)
    status = models.CharField(max_length=50)


