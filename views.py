# {{ app_name }}/views.py
from rest_framework import viewsets

# from .filters import {{ single_app_name }}Filter
from .models import {{ single_app_name }}
from .serializers import {{ single_app_name }}Serializer


class {{ camel_case_app_name }}ViewSet(viewsets.ModelViewSet):
    queryset = class {{ single_app_name }}.objects.all()
    serializer_class =  {{ single_app_name }}Serializer
    # filter_class = ()
    #
