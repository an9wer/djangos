from django.db import models


class ChoiceModel(models.Model):
    CHOICES = (
        ("a", "apple"),
        ("b", "buddy"),
    )
    field = models.CharField(max_length=20, choices=CHOICES)


"""
在 sqlite 中的创建语句如下：

CREATE TABLE "model_layer_choicemodel" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "field" varchar(20) NOT NULL);

"""


"""
关于 CHOICES:

The first element in each tuple is the actual value to be set on the model, 
and the second element is the human-readable name. 

using get_FOO_display() method can display the second element value in choice.

    >>> c = ChoiceModel(field="a")
    >>> c.save()
    >>> c.field
    'a'
    >>> c.get_field_display()
    'apple'

注意：field 的值可以不是 CHOICES 中定义的值

    >>> c = ChoiceModel(field="others")
    >>> c.save()
    >>> c.field
    'others'
    >>> c.get_field_display()
    'others'

注意：field 可以是 CHOICES tuple 中的第二个元素，但其存储到数据库中不会变成第一个
元素的值，其实第二个元素的主要目的使用在 form 中。

    >>> c = ChoiceModel(field="apple")
    >>> c.save()
    >>> c.field
    'apple'
    >>> c.get_field_display()
    'apple'

"""
