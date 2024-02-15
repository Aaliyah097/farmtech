from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=False)
        if not serializer.is_valid():
            return Response(status=400, data=serializer.errors)

        if serializer.validated_data.get("date_begin") > serializer.validated_data.get(
            "date_end"
        ):
            return Response(
                status=400, data="Дата начала должна быть раньше, чем дата окончания"
            )

        if not MeetingRoomsReservationsRepository.is_time_free(
            serializer.validated_data.get("date_begin"),
            serializer.validated_data.get("date_end"),
            serializer.validated_data.get("room").id,
        ):
            return Response(status=400, data="Переговорная на это время занята")
        return super().create(request, *args, **kwargs)
