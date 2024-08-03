from django.db import models
from .thirds import *

class Specialities(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.TextField(max_length=300)    
    
    class Meta:
        ordering = ['description']
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        
    def __str__(self):
        return self.description
    
class Services(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    speciality = models.ForeignKey(Specialities, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['description']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        
    def __str__(self):
        return self.description
    
class Fees(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    specialities = models.ForeignKey(Specialities, on_delete=models.CASCADE)
    third_entity = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Entidad",
        related_name="thirds_entity_fee",
        #limit_choices_to={"thirds__name": "Paciente"},
        null=True,
        blank=True,
    )  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    policy = models.ForeignKey('Policy', on_delete=models.PROTECT, null=True, blank=True)
    
    class Meta:
        ordering = ['description']
        verbose_name = 'Honorario'
        verbose_name_plural = 'Honorarios'
        
    def __str__(self):
        return self.description
    