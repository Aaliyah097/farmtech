from rest_framework import serializers

from src.users.models import Jobs


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = "__all__"
