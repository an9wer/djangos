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

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=50)
