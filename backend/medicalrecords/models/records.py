from django.db import models
from .thirds import Thirds

class SystemsReview(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Revision de Sistemas'
        verbose_name_plural = 'Revision de Sistemas'
        
    def __str__(self):
        return self.name

class GeneralExam(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Examen General'
        verbose_name_plural = 'Examen General'
    
    def __str__(self):
        return self.name    

class Records(models.Model):
    id = models.AutoField(primary_key=True)
    third_patient = models.ForeignKey(
        Thirds,
        on_delete=models.PROTECT,
        verbose_name="Paciente",
        related_name="thirds_patient",
        limit_choices_to={"thirds__name": "Paciente"},
        null=True,
        blank=True,
    )  
    reason_consultation = models.CharField(max_length=100)
    history = models.CharField(max_length=100)    
    systems_review = models.CharField(max_length=100)    
    general_exam = models.CharField(max_length=100)         
    types_systems_review = models.ManyToManyField(SystemsReview)
    types_general_exam = models.ManyToManyField(GeneralExam)  
    allergies = models.BooleanField()    
    third_medic = models.ForeignKey(
        Thirds,
        on_delete=models.PROTECT,
        verbose_name="Medico",
        related_name="thirds_medic",
        limit_choices_to={"thirds__name": "Medico"},
        null=True,
        blank=True,
    )     
    date_time = models.DateTimeField(auto_now_add=True)   
    diagnosis = models.ForeignKey(
        "Diagnoses",
        on_delete=models.PROTECT,
        verbose_name="Diagnostico",
        related_name="diagnosis",
        limit_choices_to={"diagnoses__name": "Diagnostico"},
        null=True,
        blank=True,
    )
    diagnosis_1 = models.ForeignKey(
        "Diagnoses",
        on_delete=models.PROTECT,
        verbose_name="Primer Diagnostico",
        related_name="diagnosis_1",
        limit_choices_to={"diagnoses__name": "Diagnostico"},
        null=True,
        blank=True,
    )
    diagnosis_2 = models.ForeignKey(
        "Diagnoses",
        on_delete=models.CASCADE,
        verbose_name="Segundo Diagnostico",
        related_name="diagnosis_2",
        limit_choices_to={"diagnoses__name": "Diagnostico"},
        null=True,
        blank=True,
    )
    diagnosis_3 = models.ForeignKey(
        "Diagnoses",
        on_delete=models.CASCADE,
        verbose_name="Tercer Diagnostico",
        related_name="diagnosis_3",
        limit_choices_to={"diagnoses__name": "Diagnostico"},
        null=True,
        blank=True,
    )
    signed=models.TextField(null=True,blank=True)
    
    
    class Meta:
        ordering = ['date_time']
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        
    def __str__(self):
        return self.reason_consultation
    