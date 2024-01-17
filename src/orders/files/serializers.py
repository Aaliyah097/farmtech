from rest_framework.serializers import ModelSerializer

from src.orders.models import OrdersFiles


class OrdersFilesSerializer(ModelSerializer):
    class Meta:
        model = OrdersFiles
        fields = "__all__"
