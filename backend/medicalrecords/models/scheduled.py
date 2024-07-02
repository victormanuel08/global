from os import utime
from django.db import models
from datetime import date


class Scheduled(models.Model):
    date = models.DateField(verbose_name="Fecha solicitada", default=date.today )
    time = models.TimeField(verbose_name="Hora")
    third_medic = models.ForeignKey(
        "Thirds",
        on_delete=models.CASCADE,
        verbose_name="Tercero Paciente",
        limit_choices_to={"thirdtypes__name": "Paciente"},
        null=True,
        blank=True,
        related_name="scheduled_patients",
    )        
    third_medic = models.ForeignKey(
        "Thirds",
        on_delete=models.CASCADE,
        verbose_name="Tercero Medico",
        limit_choices_to={"thirdtypes__name": "Medico"},
        null=True,
        blank=True,
        related_name="scheduled_medics",
    )
    speciality=models.ForeignKey(
        'Specialities',
        on_delete=models.PROTECT,
        verbose_name="Especialidad",
        null=True,
        blank=True,
        related_name='scheduled_specialities'
        )
    confirmed=models.BooleanField()
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['date', 'time']
    

    
    def __str__(self):
        return f"{self.date} - {self.time} - {self.third_patient} - {self.third_medic} - {self.speciality}"
