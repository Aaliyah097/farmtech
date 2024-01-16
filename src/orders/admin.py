from django.contrib import admin
from src.orders.models import Orders, OrdersFiles

# Register your models here.


@admin.register(OrdersFiles)
class OrderFileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrdersFiles._meta.fields]


class AdminTabularOrderFile(admin.TabularInline):
    model = OrdersFiles


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Orders._meta.fields]
    inlines = [AdminTabularOrderFile, ]
