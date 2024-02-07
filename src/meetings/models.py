from django.db import models

from src.users.models import User

# Create your models here.


class MeetingRoomsReservations(models.Model):
    date_begin = models.DateTimeField(verbose_name="Дата начала брони")
    date_end = models.DateTimeField(verbose_name="Дата окончания брони")
    is_confirmed = models.BooleanField(
        verbose_name="Подтверждено", default=False, blank=True
    )
    user = models.ForeignKey(
        to=User,
        verbose_name="Кто забронировал",
        related_name="meeting_rooms_reservations",
        on_delete=models.CASCADE,
    )
    comment = models.TextField(
        verbose_name="Комментарий", default=None, blank=True, null=True
    )

    def __str__(self):
        return f"с {self.date_begin} по {self.date_end}"

    week_days = {0: "ПН", 1: "ВТ", 2: "СР", 3: "ЧТ", 4: "ПТ", 5: "СБ", 6: "ВС"}

    class Meta:
        db_table = "meeting_rooms_reservations"
        verbose_name = "Бронь переговорной"
        verbose_name_plural = "Брони переговорной"
