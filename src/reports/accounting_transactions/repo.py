from django.db.models import QuerySet

from farmtech.base_repo import Repository
from src.reports.models import AccountingTransactions


class AccountingTransactionsRepository(Repository):
    @staticmethod
    def get_qs() -> QuerySet:
        return AccountingTransactions.objects.all()
