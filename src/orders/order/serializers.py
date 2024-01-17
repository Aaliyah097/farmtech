from rest_framework import serializers

from src.orders.files.serializers import OrdersFilesSerializer
from src.orders.models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    files = OrdersFilesSerializer(many=True, read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"
