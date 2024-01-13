from rest_framework.viewsets import ModelViewSet

from src.users.users.repo import UsersRepository
from src.users.users.serializers import UsersSerializer


class UsersView(ModelViewSet):
    queryset = UsersRepository.get_qs()
    serializer_class = UsersSerializer
