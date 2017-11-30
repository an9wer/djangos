from django.db import models


class DateTimeFieldModel(models.Model):
    field = models.DateTimeField()
    an_field = models.DateTimeField(auto_now=True)
    ana_field = models.DateTimeField(auto_now_add=True)


"""
关于 auto_now:

Automatically set the field to now every time the object is saved. Useful for
“last-modified” timestamps. The field is only automatically updated when calling
Model.save(). The field isn’t updated when making updates to other fields in
other ways such as QuerySet.update(), though you can specify a custom value for
the field in an update like that.


关于 auto_now_add:

Automatically set the field to now when the object is first created. Useful for
creation of timestamps. Note that the current datetime is always used; it’s not
just a default value that you can override. So even if you set a value for this
field when creating the object, it will be ignored. 


    >>> from django.utils import timezone
    >>> d = DateTimeFieldModel(field=timezone.now())
    >>>
    >>> # sleep(10)
    >>> d.save()
    >>> # then
    >>> print(d.field)
    2017-11-29 09:00:31.475558
    >>> print(d.an_field)
    2017-11-29 09:00:42.304080
    >>> print(d.ana_field)
    2017-11-29 09:00:42.304098
    >>>
    >>> # sleep(60)
    >>> d.save()
    >>> # then
    >>> print(d.field)
    2017-11-29 09:00:31.475558
    >>> print(d.an_field)
    2017-11-29 09:01:43.214080
    >>> print(d.ana_field)
    2017-11-29 09:00:42.304098

    在 first create 的时候，an_field 和 ana_field 在 save 的时候才会被 赋值，
    这两个值基本是相同的，而 field 会比这两个值早 10 秒左右。

    在 update 的时候，field 和 ana_field 都不会更新，而 an_field 会进行更新，
    an_field 的值比之前多 60 秒左右。


The options auto_now_add, auto_now, and default are mutually exclusive. Any
combination of these options will result in an error.(也就是 auto_now_add 和
auto_now 这两个参数不能同时定义)

"""
