from rest_framework import serializers

from src.news.models import News
from src.users.models import User
from src.users.users.serializers import UsersSerializer


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        write_only=True, required=False, many=False, queryset=User.objects.all()
    )
    author_info = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_author_info(obj):
        return UsersSerializer(obj.author).data

    class Meta:
        model = News
        fields = "__all__"
