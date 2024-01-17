from django.db import models

from src.users.models import User

# Create your models here.


class Orders(models.Model):
    STATUS_CHOICES = (
        ("new", "Новая"),
        ("accepted", "Принята"),
        ("rejected", "Отклонена"),
    )
    KIND_CHOICES = (
        ("vacation", "Отпуск"),
        ("sick_leave", "Больничный"),
        ("business_trip", "Служебная поездка"),
        ("change_of_personal_data", "Изменение персональных данных"),
        ("dismissal", "Увольнение"),
    )
    SUB_KIND_CHOICES = {
        "vacation": (
            ("regular", "Очередной"),
            ("own_expense", "За свой счет"),
            ("maternity", "Декретный"),
        ),
        "sick_leave": (("sick_leave", "Больничный"), ("maternity", "Декрет")),
        "business_trip": (
            ("by_plain", "На самолете"),
            ("by_train", "На поезде"),
            ("by_car", "На машине"),
        ),
        "change_of_personal_data": (
            ("address", "Адрес"),
            ("passport", "Паспортные данные"),
            ("contacts", "Контакты"),
        ),
        "dismissal": (("voluntary", "По собственному желанию")),
    }
    user = models.ForeignKey(
        to=User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="orders",
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    status = models.CharField(
        verbose_name="Статус", max_length=50, default="new", choices=STATUS_CHOICES
    )
    kind = models.CharField(verbose_name="Вид заявки", max_length=50)
    sub_kind = models.CharField(
        verbose_name="Тип заявки", max_length=50, default=None, blank=True, null=True
    )
    date_begin = models.DateField(verbose_name="Дата начала")
    date_end = models.DateField(verbose_name="Дата окончания")
    comment = models.TextField(
        verbose_name="Комментарий", default=None, blank=True, null=True
    )

    class Meta:
        db_table = "orders"
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class OrdersFiles(models.Model):
    order = models.ForeignKey(
        to=Orders, verbose_name="Заказ", on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(verbose_name="Файл", upload_to="files/orders/")

    class Meta:
        db_table = "orders_files"
        verbose_name = "Файлы заявки"
        verbose_name_plural = "Файлы заявок"
