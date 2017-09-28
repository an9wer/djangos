# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Abstract(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class SubAbstract(Abstract):
    age = models.PositiveIntegerField()
    
    # If a child class does not declare its own Meta class, it will inherit 
    # the parent’s Meta. If the child wants to extend the parent’s Meta class, 
    # it can subclass it. 
    #
    # the children of abstract base classes don’t automatically become abstract 
    # classes themselves. Django will set abstract=False before installing the 
    # Meta attribute of the children of abstract base classes.
    class Meta(Abstract.Meta):
        db_table = 'subabstract'
        # here the value of abstract will be setted to False hiddenly
        # abstract = False

if __name__ == "__main__":
    s = SubAbstract(name="an9wer", age=9)
    s.save()
    print s.name    # return "an9wer"
    print s.age     # return 99
