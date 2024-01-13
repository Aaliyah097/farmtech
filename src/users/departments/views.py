from rest_framework.viewsets import ModelViewSet

from src.users.departments.repo import DepartmentsRepository
from src.users.departments.serializers import DepartmentsSerializer


class DepartmentsView(ModelViewSet):
    queryset = DepartmentsRepository.get_qs()
    serializer_class = DepartmentsSerializer
