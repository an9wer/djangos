from django.db import models


class FatherAggregationModel(models.Model):
    char_field = models.CharField(max_length=20, null=True)
    int_field = models.IntegerField()

class SonAggregationModel(models.Model):
    father = models.ForeignKey(FatherAggregationModel, related_name="sons")
    char_field = models.CharField(max_length=20, null=True)
    int_field = models.IntegerField()


"""
preparation:

    >>> from django.db.models import Avg, Max, Count, Sum, FloatField
    >>>
    >>> f1 = FatherAggregationModel(int_field=100)
    >>> f1.save()
    >>> f2 = FatherAggregationModel(int_field=200)
    >>> f2.save()
    >>>
    >>> SonAggregationModel.objects.create(father=f1, int_field=101)
    >>> SonAggregationModel.objects.create(father=f1, int_field=102)
    >>> SonAggregationModel.objects.create(father=f1, int_field=103)
    >>> 
    >>> SonAggregationModel.objects.create(father=f2, int_field=201)
    >>> SonAggregationModel.objects.create(father=f2, int_field=202)

"""
