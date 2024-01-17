import django_filters

from src.users.models import Departments


class DepartmentsFilter(django_filters.FilterSet):
    class Meta:
        model = Departments
        fields = "__all__"
