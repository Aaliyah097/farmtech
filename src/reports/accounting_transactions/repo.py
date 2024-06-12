from django.db.models import QuerySet, Sum

from farmtech.base_repo import Repository
from src.reports.models import AccountingTransactions


class AccountingTransactionsRepository(Repository):
    model = AccountingTransactions

    @staticmethod
    def get_qs() -> QuerySet:
        return AccountingTransactions.objects.all()

    @classmethod
    def get_total_amount_by_balance_sheet_item(cls, item_id: int, year: int, month: int) -> int:
        return cls.model.objects.filter(
            balance_sheet_item__id=item_id,
            on_date__year=year,
            on_date__month=month
        ).aggregate(total=Sum('amount'))['total'] or 0
