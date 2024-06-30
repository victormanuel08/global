from rest_framework import viewsets
from users.serializers import GroupSerializer
from django.contrib.auth.models import Group

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.order_by('name')
    
    