from ..aggregation import FatherAggregationModel, SonAggregationModel


"""
annotate() will generate an independent summery for each object in a QuerySet.


As with aggregate(), the name for the annotation is automatically derived from
the name of the aggregate function and the name of the field being aggregated.

    >>> FatherAggregationModel.objects.annotate(Count("sons"))
    <QuerySet [<FatherAggregationModel: FatherAggregationModel object>,
    <FatherAggregationModel: FatherAggregationModel object>]>
    >>>
    >>> FatherAggregationModel.objects.annotate(Avg("sons"))[0].sons__count
    3
    >>> FatherAggregationModel.objects.annotate(Avg("sons"))[1].sons__count
    2

You can override this default name by providing an alias when you specify
the annotation:

    >>> FatherAggregationModel.objects.annotate(count=Avg("sons"))
    <QuerySet [<FatherAggregationModel: FatherAggregationModel object>,
    <FatherAggregationModel: FatherAggregationModel object>]>
    >>>
    >>> FatherAggregationModel.objects.annotate(Avg("sons"))[0].count
    3
    >>> FatherAggregationModel.objects.annotate(Avg("sons"))[1].count
    2

Unlike aggregate(), annotate() is not a terminal clause. The output of the annotate()
clause is a QuerySet; this QuerySet can be modified using any other QuerySet operation,
including filter(), order_by(), or even additional calls to annotate().

    >>> FatherAggregationModel.objects.annotate(Count("sons")).order_by("-int_field")
    <QuerySet [<FatherAggregationModel: FatherAggregationModel object>,
    <FatherAggregationModel: FatherAggregationModel object>]>
    >>>
    >>> FatherAggregationModel.objects.annotate(Avg("sons"))[0].sons__count
    2
    >>> FatherAggregationModel.objects.annotate(Avg("sons"))[1].sons__count
    3

"""


"""
annotate some value belongs to a model that is related the model you are querying:

    >>> FatherAggregationModel.objects.annotate(Max("sons__int_field"))
    <QuerySet [<FatherAggregationModel: FatherAggregationModel object>,
    <FatherAggregationModel: FatherAggregationModel object>]>
    >>> FatherAggregationModel.objects.annotate(Max("sons__int_field"))[0].sons__int_field__max
    103
    >>> FatherAggregationModel.objects.annotate(Max("sons__int_field"))[1].sons__int_field__max
    202

"""


"""
TODO:

Combining multiple aggregations with annotate() will yield the wrong results
because joins are used instead of subqueries.

    ?????

"""
