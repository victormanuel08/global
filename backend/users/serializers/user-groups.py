from rest_framework import serializers
from django.contrib.auth.models import Group ## Aca reposan todos los modelos de la autenticacion por defecto de django. usuario, grupo... etc.


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

