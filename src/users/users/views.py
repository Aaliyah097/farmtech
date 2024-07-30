from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
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

    @action(methods=["GET"], detail=False, url_path="staff")
    def my_staff(self, request, *args, **kwargs):
        user = UsersRepository.get_by_id(request.user.id)
        deps = user.deps_in_control
        staff = []
        for dep in deps:
            staff.extend(
                [{'user': u.to_dict()} | {'department': dep.to_dict()}
                 for u in dep.staff.all()]
            )
        return Response(
            status=status.HTTP_200_OK,
            data=staff
        )
