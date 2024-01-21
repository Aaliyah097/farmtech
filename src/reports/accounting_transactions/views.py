from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.reports.accounting_transactions.filters import AccountingTransactionsFilter
from src.reports.accounting_transactions.repo import AccountingTransactionsRepository
from src.reports.accounting_transactions.serializers import (
    AccountingTransactionsSerializer,
)


class AccountingTransactionsView(ModelViewSet):
    queryset = AccountingTransactionsRepository.get_qs()
    serializer_class = AccountingTransactionsSerializer
    filterset_class = AccountingTransactionsFilter
    permission_classes = [
        IsAuthenticated,
    ]
