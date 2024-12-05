from django.contrib import admin
from users.models import User, GroupDetails, PermissionsSet
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ['user_permissions']
    pass

@admin.register(PermissionsSet)
class PermissionsSetAdmin(admin.ModelAdmin):
    model = PermissionsSet
    can_delete = False
    readonly_fields = ['permissions']
    #readonly_fields = ['permissions', 'content_type']
    
class PermissionsSetInline(admin.TabularInline):
    model = PermissionsSet.groups.through
    
@admin.register(GroupDetails)
class GroupDetailsAdmin(admin.ModelAdmin):
    inlines = [PermissionsSetInline]
    readonly_fields = ['permissions']
    model = GroupDetails
    can_delete = False
    list_display = ['name', 'description', 'sets']

    def sets(self, obj):
        return [str(s) for s in obj.permissions_set.all()] if hasattr(obj, 'permissions_set') else []
