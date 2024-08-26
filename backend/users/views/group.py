from rest_framework import viewsets
from users.serializers import GroupSerializer
from django.contrib.auth.models import Group

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.order_by('name')
    
#    def partial_update(self, request, *args, **kwargs):
#        group = self.get_object()
#        updatedusers = request.data.get('users', []) 
#        group.users.set(updatedusers)
#        group.save()
#
#        return super().partial_update(request, *args, **kwargs)