# {{ app_name }}/models.py
from django.apps import AppConfig


class {{ camel_case_app_name }}(models.Model):
    # name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ("-id", )

    def __str__(self):
        # only if you uncomment name
        return self.name
