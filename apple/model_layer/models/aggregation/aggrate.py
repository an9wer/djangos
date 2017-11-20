from ..aggregation import FatherAggregationModel, SonAggregationModel


"""
aggregate() will generate summary values over an entire QuerySet.


aggregate() is a terminal clause for a QuerySet that, when invoked, returns a 
dictionary of name-value pairs. （也就是 aggregate() 后面不能再跟 order_by 等 
query method）

The name is an identifier for the aggregate value; the value is the computed aggregate.

    >>> FatherAggregationModel.objects.aggregate(Avg("int_field"))
    {'int_field__avg': 150.0}

 If you want to manually specify a name for the aggregate value, you can do so
 by providing that name when you specify the aggregate clause:

    >>> FatherAggregationModel.objects.aggregate(avg=Avg("int_field"))
    {'avg': 150.0}

If you want to generate more than one aggregate, you just add another argument
to the aggregate() clause. 

    >>> FatherAggregationModel.objects.aggregate(Avg("int_field"), Max("int_field"))
    {'int_field__avg': 150.0, 'int_field__max': 200}

"""


"""
关于 Complex aggregation:
    
    >>> FatherAggregationModel.objects.aggregate(Max("int_field")-Avg("int_field"))
    ...
    TypeError: Complex aggregates require an alias  
    
    这里需要为 complex aggregation 指定别名。


    >>> FatherAggregationModel.objects.aggregate(diff=(Max("int_field")-Avg("int_field")))
    ...
    FieldError: Expression contains mixed types. You must set output_field

    这里需要为 Max 指定 output_field，因为这里 Max 得到的是 int 类型的值，而
    Avg 得到的是 float 类型的值。


    >>> FatherAggregationModel.objects.aggregate(
    ...     diff=(Max("int_field", output_field=FloatField())-Avg("int_field")))
    50.0

"""


"""
aggregate some value belongs to a model that is related the model you are querying:

    >>> SonAggregationModel.objects.aggregate(Avg("father__int_field"))
    {'father__int_field__avg': 140.0}

    这里的 140.0 是由 (100+100+100+200+200) / 5 计算得来的。

"""
