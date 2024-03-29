from django.db import models

from {{ top_level }}.{{ app_name }}.infrastructure.querysets import {{ single_app_name }}QuerySet


class {{ single_app_name }}Manager(models.Manager):

    def get_queryset(self):
        return {{ single_app_name }}QuerySet(self.model, using=self._db)
