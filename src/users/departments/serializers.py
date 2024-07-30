from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework_recursive.fields import RecursiveField

from src.users.models import Departments, User
from src.users.users.serializers import UsersSerializer


class DepartmentsSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True, read_only=True)
    manager_info = SerializerMethodField(read_only=True)
    staff_info = SerializerMethodField(read_only=True)
    staff = serializers.PrimaryKeyRelatedField(
        write_only=True, required=False, many=True, queryset=User.objects.all()
    )
    manager = serializers.PrimaryKeyRelatedField(
        write_only=True, required=False, queryset=User.objects.all()
    )

    @staticmethod
    def get_manager_info(obj):
        return obj.manager.to_dict() if obj.manager else None
        # return UsersSerializer(obj.manager).data

    @staticmethod
    def get_staff_info(obj):
        return [u.to_dict() for u in obj.staff.all()]
        # return UsersSerializer(obj.staff, many=True).data

    class Meta:
        model = Departments
        fields = "__all__"
