import django_filters
from django_filters import FilterSet

from src.meetings.models import MeetingRoomsReservations


class MeetingRoomsReservationsFilter(FilterSet):
    date_begin = django_filters.DateFilter(lookup_expr="date__gte")
    date_end = django_filters.DateFilter(lookup_expr="date__lte")
    on_date = django_filters.DateFilter(
        field_name="date_begin", lookup_expr="date__exact"
    )

    class Meta:
        model = MeetingRoomsReservations
        fields = "__all__"
