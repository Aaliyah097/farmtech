import django_filters

from src.users.models import Regions


class RegionsFilter(django_filters.FilterSet):
    class Meta:
        model = Regions
        fields = "__all__"
