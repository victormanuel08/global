
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    
    permissions = serializers.SerializerMethodField()
    
    def get_permissions(self, obj):
        groups = obj.groups.all()
        permissions = []
        for group in groups:
            for permission in group.permissions.all():
                permissions.append(permission.name) # Todos los permisos de todos los grupos que tiene el usuario
        return set(permissions)   

    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', "permissions"]
        
        