import datetime

from django.db.models import Q

from farmtech.base_repo import Repository
from src.meetings.models import MeetingRoomsReservations


class MeetingRoomsReservationsRepository(Repository):
    @staticmethod
    def get_qs():
        return MeetingRoomsReservations.objects.all()

    @staticmethod
    def is_time_free(date_begin: datetime.datetime, date_end: datetime.datetime) -> bool:
        reservations = MeetingRoomsReservations.objects.filter(
            Q(Q(date_begin__gte=date_begin) & Q(date_begin__lte=date_end))
            | Q(Q(date_end__gte=date_begin) & Q(date_end__lte=date_end))
        ).count()

        return reservations == 0
