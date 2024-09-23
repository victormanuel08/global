from rest_framework import serializers
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _

class PermissionSerializer(serializers.ModelSerializer):
    entity_model = serializers.ReadOnlyField(source="content_type.model")
    action_name = serializers.SerializerMethodField()
    entity_name = serializers.ReadOnlyField(source="content_type.name")
    entity_app = serializers.ReadOnlyField(source="content_type.app_label")
    name_es = serializers.SerializerMethodField()  

    def get_action_name(self, obj):
        action_parts = obj.codename.split('_')
        return action_parts[0]  

    def get_name_es(self, obj):
        base_name = _(obj.name)
        words = base_name.split()

        translations = {
            'can': 'Puede',
            'add': 'Agregar',
            'change': 'Cambiar',
            'delete': 'Eliminar',
            'view': 'Ver',        
        }

        translated_words = [translations.get(word.lower(), word) for word in words]

        translated_name = ' '.join(translated_words)

        return translated_name

    class Meta:
        model = Permission
        fields = "__all__"