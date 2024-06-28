from django.db import models

# Create your models here.
class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    municipality_dane_code= models.CharField(max_length=10)
    departament_dane_code= models.CharField(max_length=10)
    region = models.CharField(max_length=100)
    departament= models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'city'
        
    def __str__(self):
        return self.name
    