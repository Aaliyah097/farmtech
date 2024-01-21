from django.db.models import QuerySet

from farmtech.base_repo import Repository
from src.reports.models import FinancialReports


class FinancialReportsRepository(Repository):
    @staticmethod
    def get_qs() -> QuerySet:
        return FinancialReports.objects.all().prefetch_related("transactions")
