from rest_framework import serializers
from farmtech import validators

from src.reports.models import ItemsLimits


class ItemsLimitsSerializer(serializers.ModelSerializer):
    month = serializers.IntegerField(validators=[validators.validate_month])

    class Meta:
        model = ItemsLimits
        fields = "__all__"
