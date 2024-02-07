from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.news.news.filters import NewsFilter
from src.news.news.repo import NewsRepository
from src.news.news.serializers import NewsSerializer


class NewsView(ModelViewSet):
    queryset = NewsRepository.get_qs()
    serializer_class = NewsSerializer
    filterset_class = NewsFilter
    permission_classes = [
        IsAuthenticated,
    ]
