from rest_framework import serializers

from src.auth2.models import Invites
from src.users.departments.serializers import DepartmentsSerializer
from src.users.jobs.serializers import JobsSerializer
from src.users.models import Departments, Jobs, User, Regions
from src.users.users.serializers import UsersSerializer
from src.users.regions.serializers import RegionsSerializer


class InvitesSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)

    user_info = serializers.SerializerMethodField(read_only=True)

    job_info = serializers.SerializerMethodField(read_only=True)
    job = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, required=False, queryset=Jobs.objects.all()
    )

    department_info = serializers.SerializerMethodField(read_only=True)
    department = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, required=False, queryset=Departments.objects.all()
    )

    region_info = serializers.SerializerMethodField(read_only=True)
    region = serializers.PrimaryKeyRelatedField(
        write_only=True, many=False, required=False, queryset=Regions.objects.all()
    )

    @staticmethod
    def get_region_info(obj):
        return RegionsSerializer(obj.region).data if obj.region else None

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

    def __init__(self, *args, **kwargs):
        super(InvitesSerializer, self).__init__(*args, **kwargs)

        if self.instance:
            self.fields['email'].required = False
