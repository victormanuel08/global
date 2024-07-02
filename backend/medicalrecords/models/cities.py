from django.db import models

# Create your models here.
class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    municipality_dane_code= models.CharField(max_length=10,blank= True, null= True)
    departament_dane_code= models.CharField(max_length=10,null= True, blank= True)
    region = models.CharField(max_length=100)
    departament= models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        
    def __str__(self):
        return self.name
    