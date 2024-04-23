from django.contrib import admin

from src.news.models import News, Trademarks

# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]


@admin.register(Trademarks)
class TrademarksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Trademarks._meta.fields]
