import django_filters

from src.reports.models import ItemsLimits


class ItemsLimitsFilter(django_filters.FilterSet):
    class Meta:
        model = ItemsLimits
        fields = "__all__"
