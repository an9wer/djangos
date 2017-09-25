# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

"""
To create a recursive relationship – an object that has a many-to-one relationship 
with itself – use models.ForeignKey('self', on_delete=models.CASCADE).
"""

class FK(models.Model):
    prev = models.ForeignKey("self", null=True, default=None, related_name="next")
