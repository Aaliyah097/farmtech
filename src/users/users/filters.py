import django_filters

from src.users.models import User


class UsersFilter(django_filters.FilterSet):
    class Meta:
        model = User
        exclude = ('photo', )
