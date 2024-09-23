from rest_framework import serializers
from django.contrib.auth.models import Group ## Aca reposan todos los modelos de la autenticacion por defecto de django. usuario, grupo... etc.


class GroupSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    
    def get_users(self, obj):
        users = obj.user_set.all()
        return [user.id for user in users]
    
    class Meta:
        model = Group
        fields = "__all__"

