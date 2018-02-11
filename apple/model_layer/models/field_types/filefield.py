from django.db import models


class FileFieldModel(models.Model):
    field = models.FileField(upload_to="filefield")


"""
class FileField(upload_to=None, max_length=100, **options)

#### upload_to

upload_to may also be a callable, such as a function. This will be called to
obtain the upload path, including the filename. This callable must accept two
arguments and return a Unix-style path (with forward slashes) to be passed
along to the storage system. The two arguments are:

1.  instance    

    An instance of the model where the FileField is defined. More specifically,
    this is the particular instance where the current file is being attached.

    In most cases, this object will not have been saved to the database yet,
    so if it uses the default AutoField, it might not yet have a value for its
    primary key field.

    注意：如果 model instance 没有 save() 是没有 id 的，所以使用这里的 instance
    的 id 属性时，可能会得到 None。

2.  filename

    The filename that was originally given to the file. This may or may not be
    taken into account when determining the final destination path.

For example:

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)

    class MyModel(models.Model):
        upload = models.FileField(upload_to=user_directory_path)


"""


"""
    >>> f = FileFieldModel()
    >>> f.field
    <FieldFile: None>

### FieldFile

When you access a FileField on a model, you are given an instance of FieldFile
as a proxy for accessing the underlying file.

The API of `FieldFile` mirrors that of `File`, with one key difference: The
object wrapped by the class is not necessarily a wrapper around Python’s
built-in `file` object. Instead, it is a wrapper around the result of the
Storage.open() method, which may be a `File` object, or it may be a custom
storage’s implementation of the `File` API.

In addition to the API inherited from File such as read() and write(),
FieldFile includes several methods that can be used to interact with the
underlying file:

-   FieldFile.name

    The name of the file including the relative path from the root of the
    Storage of the associated FileField.

-   FieldFile.size

    The result of the underlying Storage.size() method.

-   FieldFile.url

    A read-only property to access the file’s relative URL by calling the
    url() method of the underlying Storage class.

-   FieldFile.open(mode='rb')

    Opens or reopens the file associated with this instance in the specified
    mode. Unlike the standard Python open() method, it doesn’t return a file
    descriptor.

    Since the underlying file is opened implicitly when accessing it, it may
    be unnecessary to call this method except to reset the pointer to the
    underlying file or to change the mode.

-   FieldFile.close()

    Behaves like the standard Python file.close() method and closes the file
    associated with this instance.

-   FieldFile.save(name, content, save=True)

    This method takes a filename and file contents and passes them to the
    storage class for the field, then associates the stored file with the
    model field. If you want to manually associate file data with FileField
    instances on your model, the save() method is used to persist that file
    data.

    Takes two required arguments: name which is the name of the file, and
    content which is an object containing the file’s contents. The optional
    save argument controls whether or not the model instance is saved after
    the file associated with this field has been altered. Defaults to True.

    Note that the content argument should be an instance of django.core.files.File,
    not Python’s built-in file object. You can construct a File from an existing
    Python file object like this:

        from django.core.files import File
        # Open an existing file using Python's built-in open()
        f = open('/path/to/hello.world')
        myfile = File(f)

    Or you can construct one from a Python string like this:

        from django.core.files.base import ContentFile
        myfile = ContentFile("hello world")

-   FieldFile.delete(save=True)

    Deletes the file associated with this instance and clears all attributes
    on the field. Note: This method will close the file if it happens to be
    open when delete() is called.

    The optional save argument controls whether or not the model instance is
    saved after the file associated with this field has been deleted. Defaults
    to True.

    Note that when a model is deleted, related files are not deleted. If you
    need to cleanup orphaned files, you’ll need to handle it yourself (for
    instance, with a custom management command that can be run manually or
    scheduled to run periodically via e.g. cron).

"""
