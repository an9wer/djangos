from django.db import models


class DbTableModel(models.Model):
    field = models.CharField(max_length=20)

    class Meta:
        db_table = "db_table"


"""
DbTableModel 在数据库中 table name 是 db_table

To save you time, Django automatically derives the name of the database table
from the name of your model class and the app that contains it. A model’s 
database table name is constructed by joining the model’s “app label” – the 
name you used in manage.py startapp – to the model’s class name, with an 
underscore between them.

For example, if you have an app bookstore (as created by manage.py startapp 
bookstore), a model defined as class Book will have a database table named 
bookstore_book.

To override the database table name, use the db_table parameter in class Meta.

If your database table name is an SQL reserved word, or contains characters 
that aren’t allowed in Python variable names – notably, the hyphen – that’s OK.
Django quotes column and table names behind the scenes.

"""
