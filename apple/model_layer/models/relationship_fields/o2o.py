from django.db import models


class HusbandModel(models.Model):
    field = models.CharField(max_length=20)


class WifeModel(models.Model):
    husband = models.OneToOneField(HusbandModel)
    field = models.CharField(max_length=20)


class NameWifeModel(models.Model):
    husband = models.OneToOneField(HusbandModel, related_name="name_wife")
    field = models.CharField(max_length=20)


class QueryNameWifeModel(models.Model):
    husband = models.OneToOneField(HusbandModel, related_query_name="query_name_wife")
    field = models.CharField(max_length=20)


class BothNameWifeModel(models.Model):
    husband = models.OneToOneField(HusbandModel, related_name="both_name_wife",
                                   related_query_name="both_query_name_wife")
    field = models.CharField(max_length=20)


"""

关于 OneToOneField 的 related_name:

    >>> h = HusbandModel.objects.create(field="h")
    >>> w = WifeModel.objects.create(husband=h, field="w")
    >>> nw = NameWifeModel.objects.create(husband=h, field="w")
    >>> qnw = QueryNameWifeModel.objects.create(husband=h, field="qnw")
    >>> bnw = BothNameWifeModel.objects.create(husband=h, field="bnw")

使用 help(h) 可以发现 h 有三个属性：wifemodel, name_wife, querynamewifemodel,
both_name_wife 分别对应 WifeModel, NameWifeModel, QueryNameWifeModel, BothNameWifeModel
的 instance (注意：与 ForeignKey 和 ManyToManyField 不同，OneToOneField 得到的
是 Model 的 instance, 而 ForeignKey 和 ManyToManyField 得到的是 RelatedManager)

    >>> h.wifemodel
    >>> h.name_wife
    >>> h.querynamewifemodel
    >>> h.both_name_wife
"""


"""
关于 OneToOneField 的 related_query_name:

    >>> HusbandModel.objects.get(wifemodel=w)
    >>> HusbandModel.objects.get(name_wife=nw)
    >>> HusbandModel.objects.get(query_name_wife=qnw)
    >>> HusbandModel.objects.get(both_query_name_wife=bnw)

如果在 OneToOneField 中定义了 related_query_name 参数，则使用该参数的值在 Query 
中表示 Related Model，如果没有定义 related_query_name 参数则使用 related_name 参数的
值在 Query 中表示 Related Model，如果也没有定义 related_name 参数，则使用子 Model 的
名字（小写）在 Query 中表示 Related Model。

"""
