from django.db import models


# 该 model 不会校验土旁文件
class ImageFieldModel(models.Model):
    field = models.ImageField(upload_to="imagefield")


# TODO: 该 model 会校验图片文件，但有点问题
class SizedImageFieldModel(models.Model):
    h = models.PositiveIntegerField(default=30)
    w = models.PositiveIntegerField(default=40)
    field = models.ImageField(upload_to="imagefield", height_field="h", width_field="w")


"""
class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)

ImageField 也可以存储非图片类型的文件

    >>> i = ImageFieldModel()
    >>> i.field
    <ImageFieldFile: None>
    >>>
    >>> from django.core.files import File
    >>> f = File(open("./manage.py"))   # 非图片文件

    >>> i.field = f
    >>> i.save()
    >>> i.field
    <ImageFieldFile: imagefield/manage.py>
    >>>
    >>> i.field.height  # None
    >>> i.field.width   # None
    >>>
    >>> i.field.name
    'imagefield/manage.py'
    >>> i.field.url
    '/media/imagefield/manage.py'
    >>> i.field.size
    803

In addition to the special attributes that are available for FileField, an
ImageField also has "height" and "width" attributes.

To facilitate querying on those attributes, ImageField has two extra optional arguments:

-   ImageField.height_field:

    Name of a model field which will be auto-populated with the height of the
    image each time the model instance is saved.

-   ImageField.width_field:

    Name of a model field which will be auto-populated with the width of the
    image each time the model instance is saved.

ImageField instances are created in your database as varchar columns with a
default max length of 100 characters. As with other fields, you can change the
maximum length using the max_length argument.

"""
