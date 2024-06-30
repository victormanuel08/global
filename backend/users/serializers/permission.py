from rest_framework import serializers
from django.contrib.auth.models import Permission

class PermissionSerializer(serializers.ModelSerializer):
    entity_name = serializers.ReadOnlyField(source="content_type.name")
    class Meta:
        model = Permission
        fields = "__all__"