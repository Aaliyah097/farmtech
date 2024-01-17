from django.db.models import QuerySet

from farmtech.base_repo import Repository
from src.orders.models import OrdersFiles


class OrdersFilesRepository(Repository):
    @staticmethod
    def get_qs() -> QuerySet:
        return OrdersFiles.objects.all()
