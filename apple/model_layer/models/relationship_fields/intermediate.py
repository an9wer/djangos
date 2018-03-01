from django.db import models


class Person(models.Model):
    field = models.CharField(max_length=20)


class Group(models.Model):
    field = models.CharField(max_length=20)
    persons = models.ManyToManyField(Person, through="Membership", related_name="groups")


class Membership(models.Model):
    person = models.ForeignKey(Person, related_name="members")
    group = models.ForeignKey(Group, related_name="members")
    field = models.CharField(max_length=20)



"""
    >>> p1 = Person.objects.create(field="p1")
    >>> p2 = Person.objects.create(field="p2")
    >>> g1 = Group.objects.create(field="g1")
    >>> g2 = Group.objects.create(field="g2")
    >>> m1 = Membership.objects.create(person=p1, group=g1, field="m1")
    >>> m2 = Membership.objects.create(person=p2, group=g1, field="m2")

    >>> p1.groups.all()     # 包含 g1
    <QuerySet [<Group: Group object>]>
    >>> p1.members.all()    # 包含 m1
    <QuerySet [<Membership: Membership object>]>
    >>>
    >>> g1.persons.all()    # 包含 p1
    <QuerySet [<Person: Person object>]>
    >>> g1.members.all()    # 包含 m1
    <QuerySet [<Membership: Membership object>]>

### 关于 add(), create(), set(), remove(), clear()

Unlike normal many-to-many fields, you can’t use add(), create(), or set() to
create relationships(Why? You can’t just create a relationship between a Person
and a Group - you need to specify all the detail for the relationship required
by the Membership model. The simple add, create and assignment calls don’t
provide a way to specify this extra detail.):

    >>> # the following statements will not work
    >>> p1.groups.add(g1)
    >>> p1.groups.create(field="g3")
    >>> p1.groups.set([g1, g2])

The remove() method is disabled for similar reasons. For example, if the custom
through table defined by the intermediate model does not enforce uniqueness on
the (model1, model2) pair, a remove() call would not provide enough information
as to which intermediate model instance should be deleted:

    >>> Membership.objects.create(person=p1, group=g1, field="m1")
    >>> p1.groups.all()     # 包含两个 g1
    <QuerySet [<Group: Group object>, <Group: Group object>]>
    >>> # This will not work because it cannot tell which membership to remove
    >>> p1.groups.remove(g1)

However, the clear() method can be used to remove all many-to-many relationships
for an instance:

    >>> p1.groups.clear()
    >>> p1.groups.all()
    <QuerySet []>

### 关于 query

once you have established the many-to-many relationships by creating instances
of your intermediate model, you can issue queries. Just as with normal many-to-
many relationships, you can query using the attributes of the many-to-many-
related model:

    >>> Person.objects.filter(groups__field="g1")   # 包含 p1
    <QuerySet [<Person: Person object>]>

As you are using an intermediate model, you can also query on its attributes:

    >>> Person.objects.filter(members__field="m1")  # 包含 p1
    <QuerySet [<Person: Person object>]>

"""
