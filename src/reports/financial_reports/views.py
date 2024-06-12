from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.reports.financial_reports.filters import FinancialReportsFilter
from src.reports.financial_reports.repo import FinancialReportsRepository
from src.reports.financial_reports.serializers import FinancialReportsSerializer


class FinancialReportsView(ModelViewSet):
    queryset = FinancialReportsRepository().get_qs()
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
        url_path="confirm",
    )
    def confirm(self, request, pk):
        report = FinancialReportsRepository.get_by_id(pk)
        if not report:
            return Response(status=status.HTTP_404_NOT_FOUND, data="Отчет не найден")
        report.is_confirmed = True
        report.is_accounted = False
        report.save()
        return Response(status=status.HTTP_200_OK)

    @action(
        methods=[
            "POST",
        ],
        detail=True,
        url_path="unconfirm",
    )
    def unconfirm(self, request, pk):
        report = FinancialReportsRepository.get_by_id(pk)
        if not report:
            return Response(status=status.HTTP_404_NOT_FOUND, data="Отчет не найден")
        report.is_confirmed = False
        report.is_accounted = False
        report.save()
        return Response(status=status.HTTP_200_OK)

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
        report.is_confirmed = True
        report.is_accounted = True
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
        report.is_confirmed = True
        report.is_accounted = False
        report.is_locked = False
        report.save()
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_403_FORBIDDEN,
            data='Запрещено создавать отчет вручную'
        )
