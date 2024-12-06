from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.base_user import BaseUserManager


class Regions(models.Model):
    name = models.CharField(verbose_name="Название", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ragions"
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Jobs(models.Model):
    name = models.CharField(verbose_name="Название", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "jobs"
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

# TODO добавть столбец Регион и признак является ли пользователь менеджером своего региона


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None

    photo = models.ImageField(
        verbose_name="Фото", default=None, blank=True, null=True, upload_to="staff/photos"
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения", default=None, blank=True, null=True
    )

    email = models.EmailField(_("email address"), unique=True)

    middle_name = models.CharField(
        verbose_name="Отчетство", max_length=50, default=None, blank=True, null=True
    )
    job = models.ForeignKey(
        to=Jobs,
        verbose_name="Должность",
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="users",
    )
    phone = models.CharField(
        verbose_name="Телефон", max_length=25, default=None, blank=True, null=True
    )
    company = models.CharField(
        verbose_name="Компания", max_length=50, default=None, blank=True, null=True
    )
    status = models.CharField(
        verbose_name="Статус", max_length=50, default=None, blank=True, null=True
    )
    vice = models.ForeignKey(
        "User",
        verbose_name="Заместитель",
        related_name="whose_vice",
        on_delete=models.SET_NULL,
        default=None,
        blank=True,
        null=True,
    )
    manager = models.ForeignKey(
        "User",
        verbose_name="Начальник",
        related_name="who_manager",
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
    )
    region = models.ForeignKey(
        to=Regions,
        verbose_name='Регион',
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='users_in'
    )
    is_region_manager = models.BooleanField(
        verbose_name="Менеджер региона", default=False)
    employment_date = models.DateField(
        verbose_name='Дата приема на работу', default=None, blank=True, null=True
    )
    prev_eployee_fio = models.CharField(
        verbose_name="ФИО предыдущего сотрудника",
        default=None, blank=True, null=True, max_length=500
    )
    on_date = models.DateField(
        verbose_name="Дата начала периода работы", default=None, blank=True, null=True
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

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def fio(self) -> str:
        first_name = self.first_name or ""
        middle_name = self.middle_name or ""
        last_name = self.last_name or ""

        return f"{last_name} {first_name} {middle_name}"

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'fio': self.fio
        }

    @property
    def main_department(self) -> tuple['Departments', float]:
        main_dep, min_level = None, float("inf")
        for dep in self.departments.all():
            level = dep.get_level()
            if level < min_level:
                main_dep = dep
                min_level = level
        return main_dep, min_level

    @property
    def deps_in_control(self) -> list['Departments']:
        return Departments.objects.filter(
            manager__id=self.id
        )


class Departments(MPTTModel):
    name = models.CharField(
        verbose_name="Название", max_length=150, unique=True, blank=True
    )
    parent: "Departments" = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    staff = models.ManyToManyField(
        to=User, verbose_name="Сотрудники", related_name="departments", blank=True
    )
    manager = models.ForeignKey(
        to=User,
        verbose_name="Начальник",
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="in_management",
    )

    def __str__(self):
        return self.name

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name
        }

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        db_table = "departments"
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"


class NotificationsRecipients(models.Model):
    label = models.CharField(verbose_name='Название', max_length=150,
                             default=None, blank=True, null=True)
    notification = models.CharField(
        verbose_name='Источник уведомления',
        max_length=150,
    )
    recipients = models.ManyToManyField(
        User,
        verbose_name='Пользователи',
        related_name='notifications_recipients'
    )

    class Meta:
        db_table = 'notifications_recipients'
        verbose_name = verbose_name_plural = 'Получатели уведомлений'
