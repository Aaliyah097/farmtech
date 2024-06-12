from rest_framework import serializers

from src.users.models import Regions


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = "__all__"
