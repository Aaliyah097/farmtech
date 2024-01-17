from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.users.departments.filters import DepartmentsFilter
from src.users.departments.repo import DepartmentsRepository
from src.users.departments.serializers import DepartmentsSerializer


class DepartmentsView(ModelViewSet):
    queryset = DepartmentsRepository.get_qs()
    serializer_class = DepartmentsSerializer
    filterset_class = DepartmentsFilter
    permission_classes = [
        IsAuthenticated,
    ]
