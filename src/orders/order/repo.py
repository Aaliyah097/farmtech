from src.orders.models import Orders
from farmtech.base_repo import Repository


class OrdersRepository (Repository):
    @staticmethod
    def get_qs():
        return Orders.objects.all().prefetch_related("files")
