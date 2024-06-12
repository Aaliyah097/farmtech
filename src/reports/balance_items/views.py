from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.reports.balance_items.filters import BalanceItemsFilter
from src.reports.balance_items.repo import BalanceItemsRepository
from src.reports.balance_items.serializers import BalanceItemsSerializer


class BalanceItemsView(ModelViewSet):
    queryset = BalanceItemsRepository().get_qs()
    serializer_class = BalanceItemsSerializer
    filterset_class = BalanceItemsFilter
    permission_classes = [
        IsAuthenticated,
    ]
