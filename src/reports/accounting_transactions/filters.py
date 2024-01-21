import django_filters
from src.reports.models import AccountingTransactions


class AccountingTransactionsFilter(django_filters.FilterSet):
    class Meta:
        model = AccountingTransactions
        fields = '__all__'
