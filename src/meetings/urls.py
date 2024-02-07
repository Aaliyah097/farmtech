from rest_framework.routers import SimpleRouter

from src.meetings.rooms_reservations.views import MeetingRoomsReservationsView

meeting_rooms_reservations_router = SimpleRouter()
meeting_rooms_reservations_router.register(
    "meeting-rooms-reservations", MeetingRoomsReservationsView
)

urlpatterns = []
urlpatterns.extend(meeting_rooms_reservations_router.urls)
