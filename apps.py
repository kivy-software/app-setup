from django.apps import AppConfig


class {{ camel_case_app_name }}Config(AppConfig):
    name = '{{ top_level }}.{{ app_name }}'
