# {{ app_name }}/serializers.py
from rest_framework import serializers

from .models import {{ single_app_name }}


class {{ single_app_name }}Serializer(serializers.ModelSerializer):

    class Meta:
        model = {{ single_app_name }}
        fields = (
            "id",
            # "name",
        )
