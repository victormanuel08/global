from django.db import models
from datetime import date, datetime


class Scheduled(models.Model):
    date = models.DateField(verbose_name="Fecha solicitada", default=date.today )
    time = models.TimeField(verbose_name="Hora", default=datetime.now().time()) 
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
        null=True,
        blank=True,
    )
    speciality = models.ForeignKey(
        "Specialities",
        on_delete=models.PROTECT,
        verbose_name="Especialidad",
        related_name="specialities",        
    )
    confirmed=models.BooleanField()
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['date', 'time']   

    
    def __str__(self):
        return f"{self.date} - {self.time} - {self.third_patient} - {self.third_medic}"
