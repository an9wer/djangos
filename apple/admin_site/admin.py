from django.contrib import admin

from .models import AdminModel


@admin.register(AdminModel)
class AdminModelAdmin(admin.ModelAdmin):
    pass
