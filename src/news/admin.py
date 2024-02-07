from django.contrib import admin

from src.news.models import News

# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]
