from django.db import models


class TeacherModel(models.Model):
    field = models.CharField(max_length=20)


class StudentModel(models.Model):
    teachers = models.ManyToManyField(TeacherModel, related_name="students")
    field = models.CharField(max_length=20)


"""
    >>> t1 = TeacherModel.objects.create(field="t1")
    >>> s1 = StudentModel.objects.create(field="s1")
    >>> s2 = StudentModel.objects.create(field="s2")
    >>>
    >>> t1.students         # RelatedManager object
    <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager
    .<locals>.ManyRelatedManager at 0x7fddf270b4e0>
    >>> s1.teachers         # RelatedManager object
    <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager
    .<locals>.ManyRelatedManager at 0x7fddf27122e8>

add(*objs, bulk=True): Adds the specified model objects to the related object set.

    >>> t1.students.add(s1, s2)     # t1 关联 s1 和 s2
    >>> t1.students.all()           # 包含 s1 和 s2
    <QuerySet [<StudentModel: StudentModel object>, <StudentModel: StudentModel object>]>
    >>> s1.teachers.all()           # 包含 t1
    <QuerySet [<TeacherModel: TeacherModel object>]>
    >>> s2.teachers.all()           # 包含 t1
    <QuerySet [<TeacherModel: TeacherModel object>]>
    >>>
    >>> t1.students.add(s2)     # t1 关联 s2, 因为 t1 之前已经关联 s2, 所以这里不会做任何变化

    注意：add 可以一次添加一个或者多个 objects 到 related object set

create(**kwargs): Creates a new object, saves it and puts it in the related
object set. Returns the newly created object.

    >>> t2 = s1.teachers.create(field="t2")     # s1 关联 t2，并创建 t2
    >>> t2.students.all()                       # 包含 s1
    <QuerySet [<StudentModel: StudentModel object>]>

    注意：create 会在创建一个新的 object，并且添加到 related object set， 但一次只能
        操作一个 object。

remove(*objs): Removes the specified model objects from the related object set.

    >>> t1.students.remove(s1, s2)   # 删除 t1 与 s1 和 s2 的关联
    >>> t1.students.all()
    <QuerySet []>

    注意：remove 只会删除 m2m 的关联（也就是 model_layer_studentmodel_teachers），
        不会删除 TeacherModel 和 StudentModel 中的任何数据。

clear(): Removes all objects from the related object set.

    >>> t2.students.clear()         # 清空 t2 的所有关联
    >>> t2.students.all()
    <QuerySet []>

    注意：remove 只会清除 m2m 的关联（也就是 model_layer_studentmodel_teachers），
        不会删除 TeacherModel 和 StudentModel 中的任何数据。

set(objs, bulk=True, clear=False): Replace the set of related objects.

This method accepts a clear argument to control how to perform the operation. 
If False (the default), the elements missing from the new set are removed using
remove() and only the new ones are added. If clear=True, the clear() method is
called instead and the whole set is added at once.

    >>> t1.students.set([s1])       # t1 关联 s1
    >>> t1.students.all()           # 包含 s1
    <QuerySet [<StudentModel: StudentModel object>]>
    >>>
    >>> t1.students.set([s1, s2])   # t1 关联 s1, s2, 因为 t1 之前已经关联 s1，所以只添加 s2 的关联
    >>> t1.students.all()
    <QuerySet [<StudentModel: StudentModel object>, <StudentModel: StudentModel object>]>

关于 direct assignment (在 django1.10 中已经被废弃): 

    >>> t1.students = [s1, s2]      # t1 关联 s1 和 s2
    >>> t1.students.all()           # 包含 s1 和 s2
    <QuerySet [<StudentModel: StudentModel object>, <StudentModel: StudentModel object>]>

    注意：direct assignment 等价与 set()，在 django1.10 中 direct assignemnt 
        已经被废弃，所以只能使用 set()

Note that add(), create(), remove(), clear(), and set() all apply database
changes immediately for all types of related fields. In other words, there is
no need to call save() on either end of the relationship.

Also, if you are using an intermediate model for a many-to-many relationship,
then the add(), create(), remove(), and set() methods are disabled.


"""
