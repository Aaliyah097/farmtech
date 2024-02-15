from django_filters import FilterSet

from src.meetings.models import MeetingRooms


class MeetingRoomsFilter(FilterSet):
    class Meta:
        model = MeetingRooms
        fields = "__all__"
