from farmtech.base_repo import Repository
from src.meetings.models import MeetingRoomsReservations


class MeetingRoomsReservationsRepository(Repository):
    @staticmethod
    def get_qs():
        return MeetingRoomsReservations.objects.all()
