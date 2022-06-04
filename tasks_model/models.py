from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User


def _get_next_day():
    return timezone.now() + timedelta(days=1)


class Task(models.Model):
    class Status(models.IntegerChoices):
        POSTPONED = 0, _("Отложено")
        ACTIVE = 1, _("Активно")
        DONE = 2, _("Выполнено")
    title = models.CharField(max_length=256, verbose_name=_("Заголовок"))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField(default="", verbose_name=_("Задание"))
    status = models.IntegerField(default=Status.POSTPONED, choices=Status.choices, verbose_name=_("Статус"))
    importance = models.BooleanField(default=False, verbose_name=_("Важно"))
    public = models.BooleanField(default=False, verbose_name=_("Публично"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Создано"))
    deadline = models.DateTimeField(default=_get_next_day(), verbose_name=_("Выполнить до"))

    class Meta:
        verbose_name = _("Задание")
        verbose_name_plural = _("Задания")
