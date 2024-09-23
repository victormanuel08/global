from users.views import *
from rest_framework import serializers
from users.models import User, PermissionsSet
from medicalrecords.models import Thirds
from medicalrecords.serializers import ThirdSerializer
from users.serializers import GroupSerializer, PermissionSerializer
from django.contrib.auth.models import Permission



class UserSerializer(serializers.ModelSerializer):
    third = serializers.SerializerMethodField()
    menu_items = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()
    groups_full = serializers.SerializerMethodField()
    union_permissions = serializers.SerializerMethodField()
    union_permissions_all = serializers.SerializerMethodField()
    union_permissions_full = serializers.SerializerMethodField()

    def get_union_permissions_all(self, obj):
        groups_full = self.get_groups_full(obj)
        permissions = set()
        for group in groups_full:
            group_permissions = group['permissions']
            for permission in group_permissions:
                permissions.add(permission)
        return PermissionSerializer(Permission.objects.filter(id__in=permissions), many=True).data

    def get_union_permissions(self, obj):
        groups_full = self.get_groups_full(obj)
        permissions_ids = set()
        for group in groups_full:
            group_permissions_ids = group['permissions']
            for permission in group_permissions_ids:
                permissions_ids.add(permission)
        return list(permissions_ids)

    def get_union_permissions_full(self, obj):
        union_permissions_ids = self.get_union_permissions(obj)
        return PermissionSerializer(Permission.objects.filter(id__in=union_permissions_ids), many=True).data

    def get_groups_full(self, obj):
        groups = obj.groups.all()
        return GroupSerializer(groups, many=True).data


    def get_groups(self, obj):
        groups = obj.groups.all()
        return [group.id for group in groups]


    def get_third(self, obj):
        thirds = Thirds.objects.filter(user=obj)
        if thirds.exists():
            return ThirdSerializer(thirds.first()).data
        else:
            return None

    def sort_items(self, items):
        
        return sorted(items, key=lambda x: x["order_index"])

    def get_menu_items(self, obj):
        groups = obj.groups.all()
        gd = [group.groupdetails.id for group in groups]
        ps = PermissionsSet.objects.filter(groups__in=gd).order_by("id").distinct()
        
        menu_items = {}  
        missing = {}

        for p in ps:
            menu_item = {
                "path": p.path,
                "icon": p.icon,
                "order_index": p.order_index,
                "label": p.label,
                "parent_id": p.parent_id,
                "childs": [] , 
                
            }
            menu_items[p.id] = menu_item  
           

            if p.parent_id:
               
                parent_item = menu_items.get(p.parent_id)
                if parent_item:
                    parent_item["childs"].append(menu_item)
                else:
                  
                    missing[p.parent_id] = menu_item
        
     
        for parent_id, child in missing.items():
            parent_item = menu_items.get(parent_id)
            if parent_item:
                parent_item["childs"].append(child)

     
        root_items = [item for item in menu_items.values() if not item["parent_id"]]
        
        for item in root_items:
            item["childs"] = self.sort_items(item["childs"])
            
        menu_items = self.sort_items(root_items)

        return menu_items


    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "menu_items",            
            "third",
            'groups',
            'groups_full',
            'union_permissions',
            'union_permissions_all',
            'union_permissions_full',
        ]
