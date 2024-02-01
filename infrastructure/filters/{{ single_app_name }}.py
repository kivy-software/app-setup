# {{ top_level }}/infrastructure/filters/{{ single_app_name }}/{{ single_app_name }}.py

from django_filters import rest_framework as filters

from .models import {{ single_app_name }}


class {{ single_app_name}}Filter(filters.FilterSet):

    class Meta:
        model = {{ single_app_name }}
        fields = ()
