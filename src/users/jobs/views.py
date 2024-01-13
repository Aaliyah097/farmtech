from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from src.users.jobs.repo import JobsRepository
from src.users.jobs.serializers import JobsSerializer


class JobsView(ModelViewSet):
    queryset = JobsRepository.get_qs()
    serializer_class = JobsSerializer
    permission_classes = [
        IsAuthenticated,
    ]
