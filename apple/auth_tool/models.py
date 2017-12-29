from django.db import models

class CustomPermissionModel(models.Model):
    field = models.CharField(max_length=20)

    class Meta:
        permissions = (
            ("view_CP", "Can see custom permission model"),
        )


"""
默认会在 auth_permission 表中创建三个 permission: 

    add_custompermissionmodel, change_custompermissionmodel,
    delete_custompermissionmodel

再加上 Meta 中定义的 permission:

    view_CP

"""


"""
### Default permissions:

When django.contrib.auth is listed in your INSTALLED_APPS setting, it will
ensure that three default permissions – add, change and delete – are created
for each Django model defined in one of your installed applications.

These permissions will be created when you run manage.py migrate; the first
time you run migrate after adding django.contrib.auth to INSTALLED_APPS, the
default permissions will be created for all previously-installed models, as well
as for any new models being installed at that time. Afterward, it will create
default permissions for new models each time you run manage.py migrate (the
function that creates permissions is connected to the post_migrate signal).


### Programmatically creating permissions

While custom permissions can be defined within a model’s Meta class, you can
also create permissions directly. For example, you can create the can_publish
permission for a BlogPost model in myapp:

    from myapp.models import BlogPost
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType

    content_type = ContentType.objects.get_for_model(BlogPost)
    permission = Permission.objects.create(
        codename='can_publish',
        name='Can Publish Posts',
        content_type=content_type,
    )

The permission can then be assigned to a User via its `user_permissions` attribute
and `groups` attribute, or to a Group via its `permissions` attribute:

    user_instance.groups.set([group_list])
    user_instance.groups.add(group, group, ...)
    user_instance.groups.remove(group, group, ...)
    user_instance.groups.clear()
    user_instance.user_permissions.set([permission_list])
    user_instance.user_permissions.add(permission, permission, ...)
    user_instance.user_permissions.remove(permission, permission, ...)
    user_instance.user_permissions.clear()

    group_instance.permissions.set([permission_list])
    group_instance.permissions.add(permission, permission, ...)
    group_instance.permissions.remove(permission, permission, ...)
    group_instance.permissions.clear()

    以上均为 RelatedManager 的 method

"""
