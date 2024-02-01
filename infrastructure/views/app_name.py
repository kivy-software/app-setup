# {{toplevel}}/infrastructure/views/{{ app_name }}/{{ single_app_name }}.py
from rest_framework import viewsets

from {{toplevel}}.{{ app_name }}.infrastructure.filters import {{ single_app_name }}Filter
from {{toplevel}}.{{ app_name }}.infrastructure.models import {{ single_app_name }}
from {{toplevel}}.{{ app_name }}.infrastructure.serializers import {{ single_app_name }}Serializer


class {{ single_app_name }}ViewSet(viewsets.ModelViewSet):
    queryset = {{ single_app_name }}.objects.all()
    serializer_class = {{ single_app_name }}Serializer
    ordering_fields = ("id", )
    filterset_class = {{ single_app_name }}Filter
