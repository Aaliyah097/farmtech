from django.db import models

from src.users.models import Departments, Jobs, User, Regions


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
    region = models.ForeignKey(
        to=Regions,
        verbose_name='Регион',
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='invites_in'
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

    employment_date = models.DateField(
        verbose_name='Дата приема на работу', default=None, blank=True, null=True
    )
    prev_eployee_fio = models.CharField(
        verbose_name="ФИО предыдущего сотрудника",
        default=None, blank=True, null=True, max_length=500
    )
    city = models.CharField(verbose_name='Город',
                            default=None, blank=True, null=True, max_length=100)
    promotion_direction = models.CharField(
        verbose_name='Направление продвижения',
        default=None, blank=True, null=True, max_length=500
    )
    address_1 = models.TextField(
        verbose_name="Адрес для отправки пром материалов",
        default=None, blank=True, null=True
    )
    address_2 = models.TextField(
        verbose_name="Адресс для отправки СДЭК",
        default=None, blank=True, null=True
    )
    comment_1 = models.TextField(
        verbose_name="""Информации о необходимости выдачи корпоративное авто или компенсации расходов на содержание и амортизацию личного автомобиля""",
        default=None, blank=True, null=True
    )
    first_name = models.CharField(
        verbose_name='Имя', default=None, blank=True, null=True, max_length=150
    )
    last_name = models.CharField(
        verbose_name='Фамилия', default=None, blank=True, null=True, max_length=150
    )
    middle_name = models.CharField(
        verbose_name='Отчество', default=None, blank=True, null=True, max_length=150
    )
    photo = models.ImageField(
        verbose_name='Фото', default=None, blank=True, null=True, upload_to="invites/photos"
    )
    is_verified_by_hr = models.BooleanField(
        verbose_name="Согласовано кадрами", default=False, blank=True, null=True
    )
    is_verified_by_accounts = models.BooleanField(
        verbose_name="Согласовано бухгалтерией", default=False, blank=True, null=True
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения', default=None, blank=True, null=True
    )
    company = models.CharField(
        verbose_name="Компания", max_length=50, default=None, blank=True, null=True
    )

    def __str__(self):
        return f"{self.get_status_display()} {self.email}"

    class Meta:
        verbose_name = "Приглашение"
        verbose_name_plural = "Приглашения"
        db_table = "invites"
