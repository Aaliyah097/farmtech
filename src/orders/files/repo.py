from django.db.models import QuerySet

from src.orders.models import OrdersFiles
from farmtech.base_repo import Repository


class OrdersFilesRepository(Repository):
    @staticmethod
    def get_qs() -> QuerySet:
        return OrdersFiles.objects.all()
