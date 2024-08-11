from django.contrib.auth.models import Group
from django.db import models


class PermissionsSet(models.Model):
    permissions = models.ManyToManyField("auth.Permission")
    path = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
    groups = models.ManyToManyField('users.GroupDetails', blank=True, related_name='permissions_set')
    
    class Meta:
        verbose_name = "Conjunto de permisos"
        verbose_name_plural = "Conjuntos de permisos"
    
    def __str__(self):
        return f"{self.content_type.model}"
    
class GroupDetails(Group):
    description = models.TextField(default="", blank=True)
    
    def __str__(self):
        return self.group_ptr.name
    
    class Meta:
        verbose_name = "Grupo de autorización"
        verbose_name_plural = "Grupos de autorización"