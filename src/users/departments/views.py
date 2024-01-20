from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.users.departments.filters import DepartmentsFilter
from src.users.departments.repo import DepartmentsRepository
from src.users.departments.serializers import DepartmentsSerializer


class DepartmentsView(ModelViewSet):
    repository = DepartmentsRepository()
    queryset = DepartmentsRepository.get_qs()
    serializer_class = DepartmentsSerializer
    filterset_class = DepartmentsFilter
    permission_classes = [
        IsAuthenticated,
    ]

    def list(self, request, *args, **kwargs):
        return Response(
            status=200,
            data=self.serializer_class(DepartmentsRepository.tree(), many=True).data,
        )

    @action(methods=["POST"], detail=True, url_path="users/(?P<user_id>[^/.]+)")
    def add_staff(self, request, pk, user_id):
        """Добавить пользователя к департаменту"""
        DepartmentsRepository.append_staff(pk, user_id)
        return Response(status=status.HTTP_200_OK)
