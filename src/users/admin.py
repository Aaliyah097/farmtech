from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    list_filter = [
        "company",
    ]
    search_fields = ['email', ]


@admin.register(Departments)
class DepartmentAdmin(DraggableMPTTAdmin):
    list_display = ["tree_actions", "indented_title", "id", "name", "manager"]


@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Jobs)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]


@admin.register(NotificationsRecipients)
class NotificationsRecipientsAdmin(admin.ModelAdmin):
    list_display = ['notification', 'get_recipients']

    def get_recipients(self, obj):
        return str(len(obj.recipients.all()))
    get_recipients.short_description = 'Получатели'
