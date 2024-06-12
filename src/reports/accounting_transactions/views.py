from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from src.reports.financial_reports.repo import FinancialReportsRepository
from src.reports.balance_items.repo import BalanceItemsRepository

from src.reports.items_limits.repo import ItemsLimitsRepository
from src.reports.accounting_transactions.filters import AccountingTransactionsFilter
from src.reports.accounting_transactions.repo import AccountingTransactionsRepository
from src.reports.accounting_transactions.serializers import (
    AccountingTransactionsSerializer,
)
from django.db import transaction


class AccountingTransactionsView(ModelViewSet):
    queryset = AccountingTransactionsRepository.get_qs()
    serializer_class = AccountingTransactionsSerializer
    filterset_class = AccountingTransactionsFilter
    permission_classes = [
        IsAuthenticated,
    ]

    @action(
        methods=[
            "POST",
        ],
        detail=True,
        url_path="confirm",
    )
    def confirm(self, request, pk, *args, **kwargs):
        new_transaction = self.serializer_class(data=request.data)
        if not new_transaction.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data=new_transaction.errors
            )

        ex_transaction = AccountingTransactionsRepository.get_by_id(pk)
        if ex_transaction.is_confirmed:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data='Транзакция уже подтверждена'
            )
        report = FinancialReportsRepository().get_by_id(
            ex_transaction.report.id
        )
        balance_item = BalanceItemsRepository().get_by_id(
            ex_transaction.balance_sheet_item.id
        )

        if balance_item.direction:
            report.total_in += ex_transaction.amount
        else:
            report.total_out += ex_transaction.amount
        report.balance_on_end = report.total_in - report.total_out
        ex_transaction.is_confirmed = True
        ex_transaction.comment = new_transaction.validated_data['comment']

        with transaction.atomic():
            ex_transaction.save()
            report.save()

        return Response(
            status=200,
            data=self.serializer_class(instance=ex_transaction).data
        )

    def create(self, request, *args, **kwargs):
        new_transaction = self.serializer_class(data=request.data)
        if not new_transaction.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data=new_transaction.errors
            )

        report = FinancialReportsRepository().get_by_id(
            new_transaction.validated_data['report'].id
        )

        if report.is_locked:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data='ФО заблокирован для изменений'
            )

        if report.author.id != request.user.id:
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data='Изменять ФО может только создатель отчета'
            )

        balance_item = BalanceItemsRepository().get_by_id(
            new_transaction.validated_data['balance_sheet_item'].id
        )

        amount = new_transaction.validated_data['amount']

        if amount <= 0:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data='Сумма операций должна быть всегда положительной'
            )

        limit = ItemsLimitsRepository.get_limit(
            request.user.id, balance_item.id, report.year, report.month)

        if not balance_item.direction:
            total_spent = AccountingTransactionsRepository.get_total_amount_by_balance_sheet_item(
                balance_item.id,
                report.year,
                report.month
            )
        else:
            total_spent = 0

        is_confirmed = False
        if not balance_item.direction and ((total_spent + amount) > limit):
            pass
        else:
            if balance_item.direction:
                report.total_in += new_transaction.validated_data['amount']
            else:
                report.total_out += new_transaction.validated_data['amount']
            report.balance_on_end = report.total_in - report.total_out
            is_confirmed = True

        with transaction.atomic():
            new_transaction = new_transaction.save()
            if is_confirmed:
                new_transaction.is_confirmed = is_confirmed
                new_transaction.save()
            report.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data=self.serializer_class(instance=new_transaction).data
        )
