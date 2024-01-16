from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.orders.files.repo import OrdersFilesRepository
from src.orders.files.serializers import OrdersFilesSerializer


class OrdersFilesView(ModelViewSet):
    queryset = OrdersFilesRepository.get_qs()
    serializer_class = OrdersFilesSerializer
    permission_classes = [
        IsAuthenticated,
    ]
