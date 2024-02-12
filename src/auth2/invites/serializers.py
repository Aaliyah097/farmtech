from rest_framework import serializers

from src.auth2.models import Invites
from src.users.departments.serializers import DepartmentsSerializer
from src.users.jobs.serializers import JobsSerializer
from src.users.models import Departments, Jobs, User
from src.users.users.serializers import UsersSerializer


class InvitesSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        write_only=True, required=False, many=False, queryset=User.objects.all()
    )
    user_info = serializers.SerializerMethodField(read_only=True)

    job_info = serializers.SerializerMethodField(read_only=True)
    job = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, required=False, queryset=Jobs.objects.all()
    )

    department_info = serializers.SerializerMethodField(read_only=True)
    department = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, required=False, queryset=Departments.objects.all()
    )

    @staticmethod
    def get_user_info(obj):
        return UsersSerializer(obj.user).data if obj.user else None

    @staticmethod
    def get_job_info(obj):
        return JobsSerializer(obj.job).data if obj.job else None

    @staticmethod
    def get_department_info(obj):
        return DepartmentsSerializer(obj.department).data if obj.department else None

    class Meta:
        model = Invites
        fields = "__all__"
