from django.db.models import QuerySet

from farmtech.base_repo import Repository
from src.reports.models import BalanceSheetItems


class BalanceItemsRepository(Repository):
    @staticmethod
    def get_qs() -> QuerySet:
        return BalanceSheetItems.objects.all()
