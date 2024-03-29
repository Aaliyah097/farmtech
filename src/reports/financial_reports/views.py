from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.reports.accounting_transactions.serializers import (
    AccountingTransactionsSerializer,
)
from src.reports.financial_reports.filters import FinancialReportsFilter
from src.reports.financial_reports.repo import FinancialReportsRepository
from src.reports.financial_reports.serializers import FinancialReportsSerializer


class FinancialReportsView(ModelViewSet):
    queryset = FinancialReportsRepository.get_qs()
    serializer_class = FinancialReportsSerializer
    filterset_class = FinancialReportsFilter
    permission_classes = [
        IsAuthenticated,
    ]

    @action(
        methods=[
            "POST",
        ],
        detail=True,
        url_path="lock",
    )
    def lock(self, request, pk):
        report = FinancialReportsRepository.get_by_id(pk)
        if not report:
            return Response(status=status.HTTP_404_NOT_FOUND, data="Отчет не найден")
        report.is_locked = True
        report.save()
        return Response(status=status.HTTP_200_OK)

    @action(
        methods=[
            "POST",
        ],
        detail=True,
        url_path="unlock",
    )
    def unlock(self, request, pk):
        report = FinancialReportsRepository.get_by_id(pk)
        if not report:
            return Response(status=status.HTTP_404_NOT_FOUND, data="Отчет не найден")
        report.is_locked = False
        report.save()
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        В теле запроса можно передать массив транзакций.
        Они будут сохранены и прикреплены к заявке
        ```json
        "transactions": [
            {
              "balance_sheet_item": 1,
              "on_date": "2024-01-21",
              "amount": 0,
              "comment": "string"
            }
        ],
        ```
        """
        new_report = self.serializer_class(data=request.data)
        if not new_report.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=new_report.errors)
        new_report.save()

        for transaction in request.data.get("transactions", []):
            new_transaction = AccountingTransactionsSerializer(data=transaction)
            if not new_transaction.is_valid():
                return Response(
                    status=status.HTTP_400_BAD_REQUEST, data=new_transaction.errors
                )
            new_transaction.save(report=new_report.instance)

        return Response(status=status.HTTP_201_CREATED, data=new_report.data)
