import datetime
from rest_framework import serializers

from src.users.jobs.serializers import JobsSerializer
from src.users.regions.serializers import RegionsSerializer
from src.users.models import Jobs, User


class UsersSerializer(serializers.ModelSerializer):
    job_info = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(write_only=True)
    vice_info = serializers.SerializerMethodField(read_only=True)
    department_info = serializers.SerializerMethodField(read_only=True)
    manager_info = serializers.SerializerMethodField(read_only=True)
    region_info = serializers.SerializerMethodField(read_only=True)

    work_exp = serializers.SerializerMethodField(
        'get_work_exp', read_only=True
    )

    @staticmethod
    def get_region_info(obj):
        return RegionsSerializer(obj.job).data

    @staticmethod
    def get_manager_info(obj):
        if not obj.manager:
            return None
        return f"{obj.manager.last_name or ''} {obj.manager.first_name or ''} {obj.manager.middle_name or ''}"

    @staticmethod
    def get_work_exp(obj):
        if not obj.employment_date:
            return 0

        return (datetime.date.today() - obj.employment_date).days

    @staticmethod
    def get_vice_info(obj):
        if not obj.vice:
            return None
        return f"{obj.vice.last_name or ''} {obj.vice.first_name or ''} {obj.vice.middle_name or ''}"

    @staticmethod
    def get_job_info(obj):
        return JobsSerializer(obj.job).data

    @staticmethod
    def get_department_info(obj) -> dict:
        main_dep, level = obj.main_department
        if not main_dep:
            return {}
        return {
            'id': main_dep.id,
            'name': main_dep.name,
            'manager': main_dep.manager.fio if main_dep.manager else None,
        }

    class Meta:
        model = User
        fields = [field.name for field in User._meta.fields] + [
            'department_info',
            'job_info',
            'vice_info',
            'work_exp',
            'manager_info',
            'region_info'
        ]
