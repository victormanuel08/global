from rest_framework import serializers, generics
from django.contrib.auth.models import Permission
from users.serializers import PermissionSerializer

class PermissionListView(generics.ListAPIView):
    queryset = Permission.objects.filter(content_type__app_label='medicalrecords').order_by('name')
    serializer_class = PermissionSerializer