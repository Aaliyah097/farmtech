from django_filters import FilterSet

from src.orders.models import Orders


class OrdersFilter(FilterSet):
    class Meta:
        model = Orders
        fields = "__all__"
