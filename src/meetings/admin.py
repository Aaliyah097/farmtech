from django.contrib import admin

from src.meetings.models import MeetingRooms, MeetingRoomsReservations

# Register your models here.


@admin.register(MeetingRoomsReservations)
class MeetingRoomsReservationsAdmin(admin.ModelAdmin):
    list_fields = [field.name for field in MeetingRoomsReservations._meta.fields]


@admin.register(MeetingRooms)
class MeetingRoomsAdmin(admin.ModelAdmin):
    list_fields = [field.name for field in MeetingRooms._meta.fields]
