from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Jobs(models.Model):
    name = models.CharField(verbose_name="Название", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "jobs"
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class User(AbstractUser):
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

    def main_department(self):
        main_department, min_level = None, float("inf")
        for dep in self.departments.all():
            level = dep.get_level()
            if level < min_level:
                main_department = dep
                min_level = level
        return main_department, min_level


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
