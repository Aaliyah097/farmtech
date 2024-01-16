from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from src.orders.order.repo import OrdersRepository
from src.orders.order.serializers import OrdersSerializer
from src.orders.order.filters import OrdersFilter


class OrdersView(ModelViewSet):
    queryset = OrdersRepository.get_qs()
    serializer_class = OrdersSerializer
    filterset_class = OrdersFilter
    parser_classes = (FileUploadParser,)

    @action(methods=['POST'], detail=False, url_path='save-w-files')
    def save_w_files(self, request):
        files = request.FILES
        print(files)

        return Response(
            status=status.HTTP_200_OK,
        )
