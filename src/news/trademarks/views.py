from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.news.trademarks.filters import TrademarksFilter
from src.news.trademarks.repo import TrademarksRepository
from src.news.trademarks.serializers import TrademarksSerializer


class TrademarksView(ModelViewSet):
    queryset = TrademarksRepository.get_qs()
    serializer_class = TrademarksSerializer
    filterset_class = TrademarksFilter
    permission_classes = [
        IsAuthenticated,
    ]
