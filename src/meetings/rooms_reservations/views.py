from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.meetings.rooms_reservations.filters import MeetingRoomsReservationsFilter
from src.meetings.rooms_reservations.repo import MeetingRoomsReservationsRepository
from src.meetings.rooms_reservations.serializers import MeetingRoomsReservationsSerializer


class MeetingRoomsReservationsView(ModelViewSet):
    queryset = MeetingRoomsReservationsRepository.get_qs()
    serializer_class = MeetingRoomsReservationsSerializer
    filterset_class = MeetingRoomsReservationsFilter
    permission_classes = [
        IsAuthenticated,
    ]
