from django.contrib import admin

from src.auth2.models import Invites


@admin.register(Invites)
class InvitesAdmin(admin.ModelAdmin):
    list_fields = [field.name for field in Invites._meta.fields]
    list_filter = [
        "status",
    ]
