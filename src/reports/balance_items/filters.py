import django_filters
from src.reports.models import BalanceSheetItems


class BalanceItemsFilter(django_filters.FilterSet):
    class Meta:
        model = BalanceSheetItems
        fields = '__all__'
