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

再加上 Meta 中定义的一个 permission:

    view_CP

"""
