from rest_framework import serializers

from src.users.models import Departments


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"
