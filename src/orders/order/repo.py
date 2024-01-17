from farmtech.base_repo import Repository
from src.orders.models import Orders, OrdersFiles


class OrdersRepository(Repository):
    @staticmethod
    def get_qs():
        return Orders.objects.all().prefetch_related("files")

    @staticmethod
    def append_files(order_serializer_instance, file_obj):
        OrdersFiles.objects.create(order=order_serializer_instance, file=file_obj)
