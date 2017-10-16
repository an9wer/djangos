# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class O2O_Name(models.Model):
    pass

class O2O_Age(models.Model):
    # if set primary_key to True, the CREATE SQL statement will be like the following:
    # CREATE TABLE "md_o2o_age" ("name_id" integer NOT NULL PRIMARY KEY REFERENCES "md_o2o_name" ("id"));
    #
    # if set primary_key to False which is the default value, the CREATE SQL statement will be like the following:
    # CREATE TABLE "md_o2o_age" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    #                            "name_id" integer NOT NULL UNIQUE REFERENCES "md_o2o_name" ("id"));
    name = models.OneToOneField(O2O_Name, primary_key=True)

if __name__ == "__main__":
    """
    Note: if we don't specify a related_name attribute for a one-to-one field, 
    the default reverse name will be the name of the class. in this example,
    the reverse name is `o2o_age`.
    """
    n = O2O_Name()
    n.save()
    a = O2O_Age(name=name)
    a.save()
    print a.name        # return instance of O2O_Name object: n
    print n.o2o_age     # use reverse name will return instance of O2O_Age object: a
