from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.users.users.filters import UsersFilter
from src.users.users.repo import UsersRepository
from src.users.users.serializers import UsersSerializer


class UsersView(ModelViewSet):
    queryset = UsersRepository.get_qs()
    serializer_class = UsersSerializer
    filterset_class = UsersFilter
    permission_classes = [
        IsAuthenticated,
    ]
    search_fields = ["first_name", "last_name", "middle_name", "job__name"]
