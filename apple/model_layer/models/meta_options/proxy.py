from django.db import models


class ProxyModel(models.Model):
    field = models.CharField(max_length=20)


class ExtraProxyModel(ProxyModel):
    # proxy model 中不可以定义其它 field

    class Meta:
        proxy = True

    def do_something(self):
        return "done"


"""
Sometimes, however, you only want to change the Python behavior of a model – 
perhaps to change the default manager, or add a new method.

This is what proxy model inheritance is for: creating a proxy for the original
model. You can create, delete and update instances of the proxy model and all
the data will be saved as if you were using the original (non-proxied) model.
The difference is that you can change things like the default model ordering
or the default manager in the proxy, without having to alter the original.

    >>> p = ProxyModel.objects.create(field="proxy model")
    >>> p.do_something()
    ...
    AttributeError: 'ProxyModel' object has no attribute 'do_something'
    >>>
    >>> ep = ExtraProxyModel.objects.get(field="proxy model")
    >>> ep.do_something()
    "done"

"""


"""
TODO: Proxy model managers

"""
