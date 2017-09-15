# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email

# Create your models here.

class Name(models.Model):
    email = models.EmailField(validators=[validate_email])
    name = models.EmailField(null=True, validators=[validate_email])
    age = models.EmailField(validators=[validate_email])

class age(models.Model):
    email = models.EmailField(validators=[validate_email])
    #name = models.EmailField(null=True, validators=[validate_email])
    #age = models.EmailField(validators=[validate_email])

