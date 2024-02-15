from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.meetings.metting_rooms.filters import MeetingRoomsFilter
from src.meetings.metting_rooms.repo import MeetingRoomRepository
from src.meetings.metting_rooms.serializers import MeetingRoomsSerializer


class MeetingRoomsView(ModelViewSet):
    queryset = MeetingRoomRepository.get_qs()
    serializer_class = MeetingRoomsSerializer
    filterset_class = MeetingRoomsFilter
    permission_classes = [
        IsAuthenticated,
    ]
