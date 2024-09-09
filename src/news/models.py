from django.db import models

from src.users.models import User

# Create your models here.


class News(models.Model):
    author = models.ForeignKey(
        to=User,
        default=None,
        blank=True,
        null=True,
        verbose_name="Автор",
        related_name="news",
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    header = models.CharField(verbose_name="Заголовок", max_length=150)
    text = models.TextField(verbose_name="Текст", default=None, blank=True, null=True)

    def __str__(self):
        return self.header

    class Meta:
        db_table = "news"
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Trademarks(models.Model):
    STATUS_CHOICES = (("active", "Действует"), ("inactive", "Не действует"))
    description = models.TextField(
        verbose_name="Словесное описание", default=None, blank=True, null=True
    )
    mktu_cls = models.CharField(
        verbose_name="Классы МКТУ", default=None, blank=True, null=True, max_length=150
    )
    order_number = models.CharField(
        verbose_name="Номер заявки", default=None, blank=True, null=True, max_length=150
    )
    registration_number = models.CharField(
        verbose_name="Номер регистрации",
        default=None,
        blank=True,
        null=True,
        max_length=150,
    )
    owner = models.TextField(verbose_name="Владелец", default=None, blank=True, null=True)
    status = models.CharField(
        verbose_name="Статус",
        choices=STATUS_CHOICES,
        default="active",
        blank=True,
        null=False,
    )
    valid_until = models.DateField(
        verbose_name="Действует до", default=None, blank=True, null=True
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = "trademarks"
        verbose_name = "Товарный знак"
        verbose_name_plural = "Товарные знаки"


class RequestsForms(models.Model):
    user = models.ForeignKey(
        to=User,
        default=None,
        blank=True,
        null=True,
        verbose_name="Автор",
        related_name="requests_forms",
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    text = models.TextField(verbose_name="Текст", default=None, blank=True, null=True)

    class Meta:
        db_table = "requests_forms"
        verbose_name = "Обращения через форму"
        verbose_name_plural = "Обращения через форму"
