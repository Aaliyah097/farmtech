from rest_framework import serializers

from src.users.jobs.serializers import JobsSerializer
from src.users.models import Jobs, User


class UsersSerializer(serializers.ModelSerializer):
    job_info = serializers.SerializerMethodField(read_only=True)
    job = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, required=False, queryset=Jobs.objects.all()
    )
    password = serializers.CharField(write_only=True)

    @staticmethod
    def get_job_info(obj):
        return JobsSerializer(obj.job).data

    class Meta:
        model = User
        fields = "__all__"
