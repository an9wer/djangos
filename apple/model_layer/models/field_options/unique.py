from django.db import models

class UniqueModel(models.Model):
    char = models.CharField(max_length=20, unique=True)
    integer = models.IntegerField(unique=True)


class NullUniqueModel(models.Model):
    char = models.CharField(max_length=20, unique=True, null=True)
    integer = models.IntegerField(unique=True, null=True)


"""
If you try to save a model with a duplicate value in a unique field, a 
django.db.IntegrityError will be raised by the model’s save() method.

    >>> u = UniqueModel(char="char1", integer=1)
    >>> u.save()    # ok
    >>>
    >>> u = UniqueModel(char="char2", integer=1)
    >>> u.save()    # raise django.db.IntegrityError
    >>>
    >>> u = UniqueModel(char="char1", integer=2)
    >>> u.save()    # raise django.db.IntegrityError

    >>> nu = NullUniqueModel()
    >>> nu.save()   # ok
    >>>
    >>> nu = NullUniqueModel(char="char1")
    >>> nu.save()   # ok
    >>>
    >>> nu = NullUniqueModel(char="char1")
    >>> nu = NullUniqueModel(integer=1)
    >>>
    >>> nu = NullUniqueModel(char="char1")
    >>> nu.save()   # ok
    >>>
    >>> nu = NullUniqueModel(char="char1")
    >>> nu = NullUniqueModel(char="char1", integer=1)
    >>> nu.save()   # raise django.db.IntegrityError

"""
