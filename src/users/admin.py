from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Departments, Jobs, User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]


@admin.register(Departments)
class DepartmentAdmin(DraggableMPTTAdmin):
    list_display = [
        "tree_actions",
        "indented_title",
        "id",
        "name",
    ]


@admin.register(Jobs)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
