import django_filters

from src.reports.models import FinancialReports


class FinancialReportsFilter(django_filters.FilterSet):
    region = django_filters.CharFilter(
        field_name='author__region__name', lookup_expr='iexact')

    class Meta:
        model = FinancialReports
        fields = [field.name for field in FinancialReports._meta.fields] + ['region']
