from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.reports.items_limits.filters import ItemsLimitsFilter
from src.reports.items_limits.repo import ItemsLimitsRepository
from src.reports.items_limits.serializers import ItemsLimitsSerializer


class ItemsLimitsView(ModelViewSet):
    queryset = ItemsLimitsRepository().get_qs()
    serializer_class = ItemsLimitsSerializer
    filterset_class = ItemsLimitsFilter
    permission_classes = [
        IsAuthenticated,
    ]
