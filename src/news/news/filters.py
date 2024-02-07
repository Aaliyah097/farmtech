from django_filters import FilterSet

from src.news.models import News


class NewsFilter(FilterSet):
    class Meta:
        model = News
        fields = "__all__"
