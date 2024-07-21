from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


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


class User(AbstractUser):
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

    @property
    def fio(self) -> str:
        first_name = self.first_name or ""
        middle_name = self.middle_name or ""
        last_name = self.last_name or ""

        return f"{last_name} {first_name} {middle_name}"

    @property
    def main_department(self) -> tuple['Departments', float]:
        main_dep, min_level = None, float("inf")
        for dep in self.departments.all():
            level = dep.get_level()
            if level < min_level:
                main_dep = dep
                min_level = level
        return main_dep, min_level


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

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        db_table = "departments"
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
