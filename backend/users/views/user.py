from users.models import User
from users.serializers import UserSerializer

from rest_framework import viewsets, decorators, response


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True).order_by('username')
    
    @decorators.action(detail=False, methods=['get'])
    def me(self, request):
        if not request.user.is_authenticated:
            return response.Response(status=401)
        serializer = self.get_serializer(request.user)
        return response.Response(serializer.data)
    