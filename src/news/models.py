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
