from rest_framework import serializers

from src.meetings.models import MeetingRoomsReservations
from src.users.models import User
from src.users.users.serializers import UsersSerializer


class MeetingRoomsReservationsSerializer(serializers.ModelSerializer):
    week_day = serializers.SerializerMethodField(read_only=True)
    week_day_display = serializers.SerializerMethodField(read_only=True)

    user = serializers.PrimaryKeyRelatedField(
        write_only=True, required=True, many=False, queryset=User.objects.all()
    )
    user_info = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_user_info(obj):
        return UsersSerializer(obj.user).data

    @staticmethod
    def get_week_day(obj):
        return obj.date_begin.weekday()

    @staticmethod
    def get_week_day_display(obj):
        return MeetingRoomsReservations.week_days.get(obj.date_begin.weekday())

    class Meta:
        model = MeetingRoomsReservations
        fields = "__all__"
