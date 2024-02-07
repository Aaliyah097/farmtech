from django.contrib import admin

from src.meetings.models import MeetingRoomsReservations

# Register your models here.


@admin.register(MeetingRoomsReservations)
class MeetingRoomsReservationsAdmin(admin.ModelAdmin):
    list_fields = [field.name for field in MeetingRoomsReservations._meta.fields]
