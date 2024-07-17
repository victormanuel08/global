from django.db import models
from datetime import date, datetime


class Scheduled(models.Model):
    date = models.DateField(verbose_name="Fecha solicitada")
    time = models.TimeField(verbose_name="Hora") 
    third_patient = models.ForeignKey(
        "Thirds",
        on_delete=models.PROTECT,
        verbose_name="Tercero Paciente",
        related_name="scheduled_patients",
    )        
    third_medic = models.ForeignKey(
        "Thirds",
        on_delete=models.PROTECT,
        verbose_name="Tercero Medico",
        related_name="scheduled_medics",
    )
    speciality = models.ForeignKey(
        "Specialities",
        on_delete=models.PROTECT,
        verbose_name="Especialidad",
        related_name="specialities",        
    )
    record = models.ForeignKey(
        "Records",
        on_delete=models.PROTECT,
        verbose_name="Historia",
        related_name="records",
        blank=True,
        null=True,        
    )
    confirmed=models.BooleanField(null=True, blank=True)
    insurance=models.BooleanField(null=True, blank=True)
    date_origin = models.DateField(default="1999-01-01")
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['date', 'time']   

    
    def __str__(self):
        return f"{self.date} - {self.time} - {self.third_patient} - {self.third_medic}"
