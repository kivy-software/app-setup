# {{ app_name }}/models.py
from django.db import models


class {{ single_app_name }}(models.Model):
    # name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ("-id", )

    def __str__(self):
        return self.name
