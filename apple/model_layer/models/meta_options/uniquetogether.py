from django.db import models

class UniqueTogetherModel(models.Model):
    char = models.CharField(max_length=20)
    integer = models.IntegerField()

    class Meta:
        unique_together = (("char", "integer"),)


"""
    >>> u = UniqueTogetherModel(char="char1", integer=1)
    >>> u.save()    # ok
    >>>
    >>> u = UniqueTogetherModel(char="char2", integer=1)
    >>> u.save()    # ok
    >>>
    >>> u = UniqueTogetherModel(char="char1", integer=2)
    >>> u.save()    # ok
    >>>
    >>> u = UniqueTogetherModel(char="char2", integer=2)
    >>> u.save()    # ok
    >>>
    >>> u = UniqueTogetherModel(char="char2", integer=2)
    >>> u.save()    # raise django.db.IntegrityError


注意：类型是 ManyToMany 的 Field 不能用在 unique_together 中

A ManyToManyField cannot be included in unique_together. (It’s not clear what 
that would even mean!) If you need to validate uniqueness related to a 
ManyToManyField, try using a signal or an explicit through model.

The ValidationError raised during model validation when the constraint is 
violated has the unique_together error code.

"""
