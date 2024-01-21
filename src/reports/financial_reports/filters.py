import django_filters

from src.reports.models import FinancialReports


class FinancialReportsFilter(django_filters.FilterSet):
    class Meta:
        model = FinancialReports
        fields = "__all__"
