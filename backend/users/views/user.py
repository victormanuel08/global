from users.models import User
from users.serializers import UserSerializer

from rest_framework import viewsets, decorators, response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    #queryset = User.objects.filter(is_active=True).order_by('username')
    queryset = User.objects.all().order_by('username')
    search_fields = ['username', 'email','first_name','last_name']
    filterset_fields = ['is_active', 'is_staff', 'is_superuser','username']
    
    @decorators.action(detail=False, methods=['get'])
    def me(self, request):
        if not request.user.is_authenticated:
            return response.Response(status=401)
        serializer = self.get_serializer(request.user)
        return response.Response(serializer.data)
    
    def perform_create(self, serializer):
        user = serializer.save()
        user.groups.set(self.request.data.get('groups', []))
        user.save()

    def perform_update(self, serializer):
        user = serializer.save()
        user.groups.set(self.request.data.get('groups', []))
        user.save()
    
    
