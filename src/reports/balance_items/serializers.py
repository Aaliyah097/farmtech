from rest_framework import serializers

from src.reports.models import BalanceSheetItems


class BalanceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceSheetItems
        fields = "__all__"
