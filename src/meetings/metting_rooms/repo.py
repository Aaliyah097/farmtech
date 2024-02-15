from django.db.models import QuerySet

from farmtech.base_repo import Repository
from src.meetings.models import MeetingRooms


class MeetingRoomRepository(Repository):
    @staticmethod
    def get_qs() -> QuerySet:
        return MeetingRooms.objects.all()
