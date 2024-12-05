from django.contrib.auth.models import Group
from django.db import models


class PermissionsSet(models.Model):
    permissions = models.ManyToManyField("auth.Permission", blank=True)
    path = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255)
    order_index = models.IntegerField(default=0)
    label = models.CharField(max_length=255, default="", blank=True)
    content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE, null=True, blank=True)
    groups = models.ManyToManyField('users.GroupDetails', blank=True, related_name='permissions_set')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Conjunto de permisos"
        verbose_name_plural = "Conjuntos de permisos"

    def __str__(self):
        return f"{self.label if self.label else 'Sin etiqueta'}"

    
class GroupDetails(Group):
    description = models.TextField(default="", blank=True)
    
    def __str__(self):
        return self.group_ptr.name
    
    class Meta:
        verbose_name = "Grupo de autorización"
        verbose_name_plural = "Grupos de autorización"