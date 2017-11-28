from django.db import models


class FatherModel(models.Model):
    field = models.CharField(max_length=20)


class SonModel(models.Model):
    father = models.ForeignKey(FatherModel)
    field = models.CharField(max_length=20)


class NameSonModel(models.Model):
    father = models.ForeignKey(FatherModel, related_name="name_sons")
    field = models.CharField(max_length=20)


class QueryNameSonModel(models.Model):
    father = models.ForeignKey(FatherModel, related_query_name="query_name_sons")
    field = models.CharField(max_length=20)


class BothNameSonModel(models.Model):
    father = models.ForeignKey(FatherModel, related_name="both_name_sons",
                               related_query_name="both_query_name_sons")
    field = models.CharField(max_length=20)


"""
关于 related_name: The name to use for the relation from the related object back to this one.

    >>> f = Father(field="father")
    >>> f.sonmodel_set          # 得到的是 SonModel 的 RelatedManager
    >>> f.name_sons             # 得到的是 NameSonModel 的 RelatedManager
    >>> f.querynamemodel_set    # 得到的是 QueryNameSonModel 的 RelatedManager
    >>> f.both_name_sons        # 得到的是 BothNameSonModle 的 RelatedManager

使用 help(f) 可以发现 f 有四个属性：sonmodel_set, name_sons, querynamemodel_set,
both_name_sons 分别对应 SonModel, NameSonModel, QueryNameSonModel, BothNameSonModel 
这四个 model 的 RelatedManager，通过 RelatedManager 又可以得到 QuerySets。

如果没有在 ForeignKey 中定义 related_name 参数，则只能使用 FOO_set 的形式来
获取 RelatedManager

If a model has a ForeignKey, instances of the foreign-key model will have access 
to a Manager that returns all instances of the first model. By default, this 
Manager is named FOO_set, where FOO is the source model name, lowercased. This 
Manager returns QuerySets, which can be filtered and manipulated.

Example:

    >>> b = Blog.objects.get(id=1)
    >>> b.entry_set.all() # Returns all Entry objects related to Blog.

    # b.entry_set is a Manager that returns QuerySets.
    >>> b.entry_set.filter(headline__contains='Lennon')
    >>> b.entry_set.count()

You can override the FOO_set name by setting the related_name parameter in the 
ForeignKey definition. For example, if the Entry model was altered to 
blog = ForeignKey(Blog, on_delete=models.CASCADE, related_name='entries'), 
the above example code would look like this:

        >>> b = Blog.objects.get(id=1)
        >>> b.entries.all() # Returns all Entry objects related to Blog.

        # b.entries is a Manager that returns QuerySets.
        >>> b.entries.filter(headline__contains='Lennon')
        >>> b.entries.count()
"""

# -------------------------------------------------------------------------- #

"""
关于 related_query_name: The name to use for the reverse filter name from the target model. 

    >>> FatherModel.objects.filter(sonmodel=XXX)
    >>> FatherModel.objects.filter(name_sons=XXX)
    >>> FatherModel.objects.filter(query_name_sons=XXX)
    >>> FatherModel.objects.filter(both_query_name_sons=XXX)

    其中：XXX 是各个 Son Model 的 instance。

如果在 ForeignKey 中定义了 related_query_name 参数，则使用该参数的值在 Query 
中表示子 Model，如果没有定义 related_query_name 参数则使用 related_name 参数的
值在 Query 中表示子 Model，如果也没有定义 related_name 参数，则使用子 Model 的
名字（小写）在 Query 中表示子 Model。

The name to use for the reverse filter name from the target model. It defaults 
to the value of related_name or default_related_name if set, otherwise it 
defaults to the name of the model
"""


"""
关于 RelatedManager:

    >>> f1 = FatherModel.objects.create(field="f1")
    >>> s1 = SonModel.objects.create(field="s1", father=f1)
    >>>
    >>> f1.sonmodel_set
    <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager
    .<locals>.RelatedManager at 0x7fddf2791710>   
    >>>
    >>> s1.father
    <FatherModel: FatherModel object>

    也就是 f1.sonmodel_set 得到的是 RelatedManager 对象，s1.father 得到的是 
    FatherModel 对象
"""
