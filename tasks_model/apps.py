from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TasksModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks_model'
    verbose_name = _("Список дел")
