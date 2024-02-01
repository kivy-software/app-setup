# {{toplevel}}/infrastructure/views/{{ app_name }}/{{ single_app_name }}.py
from rest_framework import viewsets

# from .filters import {{ single_app_name }}Filter
from .models import {{ single_app_name }}
from .serializers import {{ single_app_name }}Serializer


class {{ single_app_name }}ViewSet(viewsets.ModelViewSet):
    queryset = {{ single_app_name }}.objects.all()
    serializer_class = {{ single_app_name }}Serializer
    ordering_fields = ("id", )
    # filter_class = {{ single_app_name }}Filter
