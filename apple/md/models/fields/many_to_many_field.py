# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# TODO: intermediate model 中的两个联合外键可以重复？


class M2M_Person(models.Model):
    name  = models.CharField(max_length=128)

class M2M_Group(models.Model):
    name = models.CharField(max_length=128)
    persons = models.ManyToManyField(
        M2M_Person, through="M2M_Membership", related_name='groups')

# an intermediate model
class M2M_Membership(models.Model):
    person = models.ForeignKey(M2M_Person)
    group = models.ForeignKey(M2M_Group)
    # we can define extra field in intermedia model
    status = models.CharField(max_length=50)


