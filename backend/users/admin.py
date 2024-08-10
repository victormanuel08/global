from django.contrib import admin
from users.models import User, GroupDetails
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

class GroupDetailsInline(admin.StackedInline):
    model = GroupDetails
    can_delete = False
    verbose_name_plural = 'group details'
    
@admin.register(Group)
class GroupCustomAdmin(admin.ModelAdmin):
    inlines = (GroupDetailsInline,)
    
    