from django.contrib import admin

from src.news.models import News, Trademarks, RequestsForms

# Register your models here.


@admin.register(RequestsForms)
class RequestsFormsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RequestsForms._meta.fields]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]


@admin.register(Trademarks)
class TrademarksAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Trademarks._meta.fields]
