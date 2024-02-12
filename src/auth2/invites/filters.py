import django_filters

from src.auth2.models import Invites


class InvitesFilter(django_filters.FilterSet):
    class Meta:
        model = Invites
        fields = "__all__"
