from django.contrib.auth.models import Group
from django.db import models


class PermissionsSet(models.Model):
    permissions = models.ManyToManyField("auth.Permission")
    path = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    groups = models.ManyToManyField('users.GroupDetails', blank=True, related_name='permissions_set')
    
    def __str__(self):
        return self.path

class GroupDetails(Group):
    description = models.TextField()
    
    def __str__(self):
        return self.group_ptr.name
    
    class Meta:
        verbose_name = "Grupo de autorización"
        verbose_name_plural = "Grupos de autorización"