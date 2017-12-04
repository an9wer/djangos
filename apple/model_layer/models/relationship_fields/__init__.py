from .o2o import (
    HusbandModel, WifeModel, NameWifeModel,
    QueryNameWifeModel, BothNameWifeModel)
from .foreignkey import (
    FatherModel, SonModel, NameSonModel,
    QueryNameSonModel, BothNameSonModel)
from .m2m import TeacherModel, StudentModel


"""
A “related manager” is a manager used in a one-to-many or many-to-many related
context. This happens in two cases:

-   The “other side” of a ForeignKey relation. That is:

        from django.db import models

        class Reporter(models.Model):
            pass

        class Article(models.Model):
            reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    In the above example, the methods below will be available on the manager
    `reporter.article_set`.

-   Both sides of a ManyToManyField relation:

        class Topping(models.Model):
            pass

        class Pizza(models.Model):
            toppings = models.ManyToManyField(Topping)

    In this example, the methods below will be available both on 
    `topping.pizza_set` and on `pizza.toppings`.

"""


"""
class ManyRelatedManager(django.db.models.manager.Manager)
    # Method resolution order:
    #     ManyRelatedManager
    #     django.db.models.manager.Manager
    #     django.db.models.manager.BaseManagerFromQuerySet
    #     django.db.models.manager.BaseManager
    #     builtins.object

"""
