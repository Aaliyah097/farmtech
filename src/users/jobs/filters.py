import django_filters
from src.users.models import Jobs


class JobsFilter(django_filters.FilterSet):
    class Meta:
        model = Jobs
        fields = '__all__'
