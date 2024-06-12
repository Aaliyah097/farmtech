from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.users.regions.filters import RegionsFilter
from src.users.regions.repo import RegionsRepository
from src.users.regions.serializers import RegionsSerializer


class RegionsView(ModelViewSet):
    queryset = RegionsRepository.get_qs()
    serializer_class = RegionsSerializer
    filterset_class = RegionsFilter
    permission_classes = [
        IsAuthenticated,
    ]
