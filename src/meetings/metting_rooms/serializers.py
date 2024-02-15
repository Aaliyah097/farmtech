from rest_framework import serializers

from src.meetings.models import MeetingRooms


class MeetingRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRooms
        fields = "__all__"
