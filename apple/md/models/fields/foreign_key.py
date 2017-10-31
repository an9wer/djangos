# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class FK_One(models.Model):
    pass

class FK_Many(models.Model):
    # The name to use for the reverse filter name from the target model. 
    # It defaults to the value of related_name or default_related_name if set, 
    # otherwise it defaults to the name of the model
    one = models.ForeignKey(FK_One, related_name="many")
