from rest_framework.routers import SimpleRouter

from src.meetings.metting_rooms.views import MeetingRoomsView
from src.meetings.rooms_reservations.views import MeetingRoomsReservationsView

meeting_rooms_reservations_router = SimpleRouter()
meeting_rooms_reservations_router.register(
    "meeting-rooms-reservations", MeetingRoomsReservationsView
)

meetings_rooms_router = SimpleRouter()
meetings_rooms_router.register("meeting-room", MeetingRoomsView)

urlpatterns = []
urlpatterns.extend(meeting_rooms_reservations_router.urls)
urlpatterns.extend(meetings_rooms_router.urls)
