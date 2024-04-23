import django_filters

from src.news.models import Trademarks


class TrademarksFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(
        field_name="description", lookup_expr="icontains"
    )
    owner = django_filters.CharFilter(field_name="owner", lookup_expr="icontains")
    valid_until_gte = django_filters.DateFilter(
        field_name="valid_until", lookup_expr="gte"
    )
    valid_until_lte = django_filters.DateFilter(
        field_name="valid_until", lookup_expr="lte"
    )

    class Meta:
        model = Trademarks
        fields = "__all__"
