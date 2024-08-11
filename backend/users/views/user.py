from users.models import User
from users.serializers import UserSerializer

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True).order_by('username')