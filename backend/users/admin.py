from django.contrib import admin
from users.models import User, GroupDetails, PermissionsSet
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

@admin.register(PermissionsSet)
class PermissionsSetAdmin(admin.ModelAdmin):
    model = PermissionsSet
    can_delete = False
    
class PermissionsSetInline(admin.TabularInline):
    model = PermissionsSet.groups.through
    
@admin.register(GroupDetails)
class GroupDetailsAdmin(admin.ModelAdmin):
    inlines = [PermissionsSetInline]
    model = GroupDetails
    can_delete = False
    