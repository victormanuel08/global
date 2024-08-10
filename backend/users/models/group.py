from django.contrib.auth.models import Group
from django.db import models

class GroupDetails(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.group.name