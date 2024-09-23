from rest_framework import serializers, generics

from users.serializers import PermissionSerializer
from django.contrib.auth.models import Permission 

class PermissionListView(generics.ListAPIView):
    queryset = Permission.objects.filter(content_type__app_label='medicalrecords').order_by('name')
    serializer_class = PermissionSerializer