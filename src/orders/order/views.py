from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from farmtech.settings import logger
from src.orders.order.filters import OrdersFilter
from src.orders.order.repo import OrdersRepository
from src.orders.order.serializers import OrdersSerializer


class OrdersView(ModelViewSet):
    queryset = OrdersRepository.get_qs()
    serializer_class = OrdersSerializer
    filterset_class = OrdersFilter
    parser_classes = (MultiPartParser,)
    permission_classes = [
        IsAuthenticated,
    ]

    def create(self, request, *args, **kwargs):
        new_order = self.serializer_class(data=request.data)
        if not new_order.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=new_order.errors)
        new_order.save()

        for filename, file in request.FILES.items():
            logger.info(f"file {filename}, {file}")
            OrdersRepository.append_files(new_order.instance, file)

        return Response(status=status.HTTP_201_CREATED, data=new_order.data)
