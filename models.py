# {{ app_name }}/models.py
from django.db import models

# from .managers import {{ single_app_name }}Manager


class {{ single_app_name }}(models.Model):
    # name = models.CharField(max_length=150, unique=True)

    # objects = {{ single_app_name }}Manager()

    class Meta:
        ordering = ("-id", )

    def __str__(self):
        return self.name
