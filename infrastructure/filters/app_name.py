from django_filters import rest_framework as filters

from {{app_name}}.models import {{ single_app_name }}


class {{ single_app_name}}Filter(filters.FilterSet):

    class Meta:
        model = {{ single_app_name }}
        fields = ()
