from rest_framework import serializers

from src.users.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
