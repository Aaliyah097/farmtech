from django.db import models

from src.users.models import Departments, Jobs, User


class Invites(models.Model):
    STATUS_CHOICES = (
        ("new", "Ожидает подтверждения"),
        ("confirmed", "Подтверждена"),
        ("rejected", "Отклонена"),
    )
    email = models.EmailField(verbose_name="Email", unique=True)
    phone = models.CharField(
        verbose_name="Телефон", max_length=20, default=None, blank=True, null=True
    )
    status = models.CharField(
        verbose_name="Статус",
        max_length=50,
        choices=STATUS_CHOICES,
        default="new",
        blank=True,
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    user = models.ForeignKey(
        verbose_name="Пригласивший",
        to=User,
        related_name="invites",
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )
    manager = models.ForeignKey(
        verbose_name="Начальник",
        to=User,
        related_name="invites_manager",
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )
    on_date = models.DateField(
        verbose_name="Дата начала периода работы", default=None, blank=True, null=True
    )
    region = models.CharField(
        verbose_name="Регион", max_length=150, default=None, blank=True, null=True
    )
    department = models.ForeignKey(
        verbose_name="Отдел",
        to=Departments,
        related_name="invites_for_department",
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )
    job = models.ForeignKey(
        verbose_name="Должность",
        to=Jobs,
        related_name="invites_for_job",
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.get_status_display()} {self.email}"

    class Meta:
        verbose_name = "Приглашение"
        verbose_name_plural = "Приглашения"
        db_table = "invites"
