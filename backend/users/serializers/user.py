
from rest_framework import serializers
from django.contrib.auth.models import User
from medicalrecords.models import Thirds
from medicalrecords.serializers import ThirdSerializer


class UserSerializer(serializers.ModelSerializer):
    third = serializers.SerializerMethodField()
    permissions = serializers.SerializerMethodField()
    
    def get_third(self, obj):
        thirds = Thirds.objects.filter(user = obj) 
        if thirds.exists():
            return ThirdSerializer(thirds.first()).data
        else:
            return None   
        
    def get_permissions(self, obj):
        groups = obj.groups.all()
        permissions = []
        for group in groups:
            for permission in group.permissions.all():
                permissions.append(permission.name) # Todos los permisos de todos los grupos que tiene el usuario
        return set(permissions)   

    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', "permissions", 'third']
        
        