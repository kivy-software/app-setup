# {{ app_name }}/managers.py
from django.db import models

from .querysets import {{ single_app_name }}Manager


class {{ single_app_name }}Manger(models.Manager):

    def get_queryset(self):
        return {{ single_app_name }}QuerySet(self.model, using=self._db)
