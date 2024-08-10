from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
from .specialities import *

from django.db.models.signals import post_save
from django.dispatch import receiver

PRIORITY_CHOICES = (
    ('W', 'Blanco'),
    ('R', 'Rojo'),
    ('Y', 'Amarillo'),
    ('G', 'Verde'),
    ('B', 'Negro'),
)

RELATIONSHIP_CHOICES = (
    ('PA', 'PADRE'),
    ('MA', 'MADRE'),
    ('HO', 'HIJO'),
    ('HE', 'HERMAN@'),    
    ('SO', 'SOBRIN@'),
    ('CO', 'CONYUGE'),
    ('PR', 'PRIM@'),
    ('AB', 'ABUEL@'),
    ('NI', 'NIET@'),   
    ('TI', 'TI@'),   
    ('SU', 'SUEGR@'),   
    ('CU', 'CUÑAD@'),
    ('OT', 'OTRO'),    
)

EXTERNAL_CAUSE_CHOICES = (
    ('GE', 'ENF GENERAL'),
    ('CA', 'ACCIDENTE COMUN'),
    ('TA', 'ACCIDENTE TRANSITO'),
    ('AG', 'LESION AGRESION'),
    ('AU', 'LESION AUTOINFLINGIDA'),
    ('CA', 'CATASTROFE'),
    ('LA', 'ACCIDENTE LABORAL'),
    ('RB', 'ACC RBICO U OFIDICO'),
    ('OT', 'OTRO')
)

VEHICLE_TYPE_CHOICES = (
    ('AU', 'AUTOMOVIL'),
    ('MO', 'MOTO'),
    ('CA', 'CAMIONETA'),
    ('BU', 'BUS'),
    ('CA', 'CAMION'),
    ('OT', 'OTRO'),    
)

GLASGOW_RO_CHOICES = (
    ('4', 'ESPOTANEA'),
    ('3', 'A ESTIMULO VERBAL'),
    ('2', 'A ESTIMULO DOLOROSO'),
    ('1', 'NINGUNA')
)

GLASGOW_RV_CHOICES = (
    ('5', 'ORIENTADO'),
    ('4', 'CONFUSO'),
    ('3', 'PALABRAS INADECUADAS'),
    ('2', 'SONIDOS INADECUADOS'),
    ('1', 'NINGUNA')
)

GLASGOW_RM_CHOICES = (
    ('6', 'OBEDECE ORDENES'),
    ('5', 'LOCALIZA DOLOR'),
    ('4', 'FLEXION NORMAL'),
    ('3', 'FLEXION ANORMAL'),
    ('2', 'EXTENSION'),
    ('1', 'NINGUNA')
)

HALF_CHOICES = (
    ('TE', 'Telfonico'),
    ('RA', 'Padio'),
    ('PE', 'Personal'),
    ('OB', 'Observado')
)

BODY_PART_CHOICES = (
    ('CA', 'Cabeza', '3,15,10,22', '3,4,15,16,9,10,21,22'),
    ('CU', 'Cuello', '27,34', '27,28,33,34'),
    ('TO', 'Torax','',''),
    ('DO', 'Dorso','',''),
    ('AB', 'Abdomen','63,75,87','75,76'),
    ('PE', 'Pelvis/Perine','99,98,100','87,88'),
    ('MI', 'Miembro Inferior','105,106,107,110,111,112,118,117,119,129,130,131,141,142,153,154,155,165,166,167,122,123,124,135,147,159,171,178,177,183','99,100,111,112,123,124,135,136,147,148,159,160,171,172,183,184,105,106,117,118,129,130,141,142,153,154,165,166,177,178,189,190'),
    ('SU', 'Miembro Superior','',''),
)

BODY_PART_SIDE_CHOICES = (
    ('GL', 'Glutea','105,106,107','93,94,105,106'),
    ('AM', 'Anterior Muslo','122,123,124,110,111,112','99,100,101,111,112,123,124'),
    ('PM', 'Posterior Muslo','118,117,119,129,130,131','117,118,116,129,130'),
    ('AR', 'Anterior Rodilla','135','135,136'),
    ('PR', 'Posterior Rodilla','141,142','141,142'),
    ('AP', 'Anterior Pierna','147,159','159,160,147,148'),
    ('PP', 'Posterior Pierna','153,154,155,165,166,167','153,154,165,166'),
    ('TA', 'Tobillo anterior','171','171,172'),
    ('TP', 'Tobullo posterior','178,177','177,178'),
    ('PI', 'Pie','183',''),
)   

PAYMENT_MODEL_CHOICES = (
    ('FF', 'FONDO FIJO'),
    ('EV', 'EVENTO'),
)

TYPE_POLICE_CHOICES = (
    ('SE', 'SOAT'),
    ('AD', 'ADRES'),
    ('EP', 'EAPB'), 
    ('PA', 'PARTICULAR'), 
    ('EZ', 'ZONA SEGURA'),
    ('AR', 'ARL'),
    ('MP', 'MEDICINA PREPAGADA'),
    ('VI', 'VINCULADOS'),
)

VALUES_CHOICES = {
    ('SE', 'SOAT'),
    ('FO', 'FOSIGA-ECAT'),
    ('SM', 'SALARIO MINIMO'),
}
    

    

class Procedures(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Procedimiento'
        verbose_name_plural = 'Procedimientos'
        
    def __str__(self):
        return self.name    
    
class Vehicles(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=2,choices=VEHICLE_TYPE_CHOICES)
    third_driver = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Conductor",
        related_name="thirds_driver_vehicle",
        #limit_choices_to={"thirds__name": "Paciente"},
        null=True,
        blank=True,
    )  
    
    class Meta:
        ordering = ['brand']
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        
    def __str__(self):
        return self.brand

class Policy(models.Model):    
    description= models.CharField(max_length=30)
    name= models.CharField(max_length=100,default='Contrato')
    third_entity = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Entidad",
        related_name="thirds_policy_entity",
        #limit_choices_to={"thirds__name": "Entidad"},
    )
    vehicle = models.ForeignKey('Vehicles', on_delete=models.PROTECT, null=True, blank=True)
    date_start = models.DateField(default=datetime(datetime.now().year, 1, 1))
    date_end = models.DateField(default=datetime(datetime.now().year, 12, 31))    
    payment_model = models.CharField(max_length=2,choices=PAYMENT_MODEL_CHOICES, default='SE')
    type_police= models.CharField(max_length=2,choices=TYPE_POLICE_CHOICES, default='SE')
    amount_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)   
    amount_affection = models.DecimalField(max_digits=12, decimal_places=2, default=0)
   
    template= models.BooleanField(default=False)
    template_origin= models.ForeignKey('Policy', on_delete=models.PROTECT, null=True, blank=True)
    
    class Meta:
        ordering = ['description']
        verbose_name = 'Poliza'
        verbose_name_plural = 'Polizas'
        
    def __str__(self):
        return self.description
    
    
@receiver(post_save, sender=Policy)
def create_fees_for_policy(sender, instance, created, **kwargs):
    
    # ACA CUANDO CREO UNA POLIZA Y  TIENE PLANTILLA
    if created and instance.template_origin:   
        existing_fees = Fees.objects.filter(policy=instance.template_origin)
        for fee in existing_fees:  
            amountFee = fee.amount   
            if instance.amountFee > 0:    
                Fees.objects.create(                
                    service=fee.service,
                    specialities=fee.specialities,
                    third_entity=instance.third_entity,
                    amount=amountFee, 
                    policy=instance,
                )
    # ACA ES PARA CUANDO CREO UNA PLANTILLA DE POLIZA    
    if created and instance.template and instance.type_police == 'SE' and instance.payment_model == 'SE':
        all_services = Services.objects.all()
        for service in all_services:
            specialitiesService = service.speciality
            Fees.objects.create(                
                service=service,
                specialities=specialitiesService,
                third_entity=instance.third_entity,
                amount= 0, 
                policy=instance,
                )   



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
    
class Records_details(models.Model):   
    record = models.ForeignKey(
         'Records',
        on_delete=models.PROTECT,
        verbose_name="Registro",
        related_name="Records",      
    )     
    observation = models.CharField(max_length=100,)
    date_time = models.DateTimeField(auto_now_add=True)
    signed=models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'Detalle de Registro'
        verbose_name_plural = 'Detalle de Registros'
    
    def __str__(self):
        return self.observation

class Records(models.Model):
    id = models.AutoField(primary_key=True)
    third_patient = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Paciente",
        related_name="thirds_patient",
        #limit_choices_to={"thirds__name": "Paciente"},
        null=True,
        blank=True,
    )  
    reason_consultation = models.CharField(max_length=100,null=True, blank=True)
    history = models.CharField(max_length=100,null=True, blank=True)    
    systems_review = models.CharField(max_length=100,null=True, blank=True)    
    general_exam = models.CharField(max_length=100,null=True, blank=True)         
    types_systems_review = models.ManyToManyField(SystemsReview, null=True, blank=True)
    types_general_exam = models.ManyToManyField(GeneralExam, null=True, blank=True)
    third_medic = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Medico",
        related_name="thirds_medic",
        #limit_choices_to={"thirds__name": "Medico"},
        null=True,
        blank=True,
    )     
    third_medic_clinic = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Medico",
        related_name="thirds_medic_clinic",
        #limit_choices_to={"thirds__name": "Medico"},
        null=True,
        blank=True,
    )  
    date_time = models.DateTimeField(auto_now_add=True)   
    diagnosis = models.ForeignKey(
        "Diagnoses",
        on_delete=models.PROTECT,
        verbose_name="Diagnostico",
        related_name="diagnosis",
        #limit_choices_to={"diagnoses__name": "Diagnostico"},
        null=True,
        blank=True,
    )
    diagnosis_1 = models.ForeignKey(
        "Diagnoses",
        on_delete=models.PROTECT,
        verbose_name="Primer Diagnostico",
        related_name="diagnosis_1",
        #limit_choices_to={"diagnoses__name": "Diagnostico"},
        null=True,
        blank=True,
    )
    diagnosis_2 = models.ForeignKey(
        "Diagnoses",
        on_delete=models.CASCADE,
        verbose_name="Segundo Diagnostico",
        related_name="diagnosis_2",
        #limit_choices_to={"diagnoses__name": "Diagnostico"},
        null=True,
        blank=True,
    )
    diagnosis_3 = models.ForeignKey(
        "Diagnoses",
        on_delete=models.CASCADE,
        verbose_name="Tercer Diagnostico",
        related_name="diagnosis_3",
        #limit_choices_to={"diagnoses__name": "Diagnostico"},
        null=True,
        blank=True,
    )    
    signed=models.TextField(null=True,blank=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, null=True, blank=True)
    relationship = models.CharField(max_length=2,choices=RELATIONSHIP_CHOICES,null=True, blank=True)
    external_cause=models.CharField(max_length=2,choices=EXTERNAL_CAUSE_CHOICES,null=True, blank=True)
    city = models.ForeignKey("Cities", on_delete=models.PROTECT, null=True, blank=True)
    zone = models.CharField(max_length=10,null=True, blank=True)
    # third_relationship = models.ForeignKey(
    #    'Thirds',
    #    on_delete=models.PROTECT,
    #    verbose_name="Acompañante",
    #    related_name="thirds_relationship",
    #    #limit_choices_to={"thirds__name": "Medico"},
    #    null=True,
    #    blank=True,
    #)
    third_entity = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Entidad",
        related_name="thirds_entity",
        #limit_choices_to={"thirds__name": "Medico"},
        null=True,
        blank=True,
    )
    policy = models.ForeignKey(
        'Policy',
        on_delete=models.PROTECT,
        verbose_name="Poliza",
        related_name="policy",
        #limit_choices_to={"thirds__name": "Medico"},
        null=True,
        blank=True,
    )
    ef_fc = models.CharField(max_length=10,null=True, blank=True)
    ef_fr = models.CharField(max_length=10,null=True, blank=True)
    ef_pa = models.CharField(max_length=10,null=True, blank=True)
    ef_temp = models.CharField(max_length=10,null=True, blank=True)
    glasgow_ro = models.CharField(max_length=10,choices=GLASGOW_RO_CHOICES,null=True, blank=True)
    glasgow_rv = models.CharField(max_length=10,choices=GLASGOW_RV_CHOICES,null=True, blank=True)
    glasgow_rm = models.CharField(max_length=10,choices=GLASGOW_RM_CHOICES,null=True, blank=True)
    procedures = models.ManyToManyField(Procedures, null=True, blank=True)
    procedures_others=models.CharField(max_length=300,null=True, blank=True)

    half = models.CharField(max_length=2,choices=HALF_CHOICES,null=True, blank=True)
    time_start = models.TimeField( null=True, blank=True)
    time_end = models.TimeField( null=True, blank=True)
    condition = models.CharField(max_length=100,null=True, blank=True)
    third_clinic = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Clinica",
        related_name="thirds_clinic",
        #limit_choices_to={"thirds__name": "Medico"},
        null=True,
        blank=True,
    )
    live = models.BooleanField(null=True, blank=True)
    signed_driver=models.TextField(null=True,blank=True)
    signed_recived=models.TextField(null=True,blank=True)  
    # signed_profesional_send=models.TextField(null=True,blank=True)  
    obj= models.BooleanField(null=True, blank=True)
    value_obj=models.CharField(max_length=200,null=True, blank=True) 
    third_obj = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Pertenencias",
        related_name="thirds_objects",
        #limit_choices_to={"thirds__name": "Medico"},
        null=True,
        blank=True,
    )
    third_driver = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Conductor",
        related_name="thirds_driver",
        #limit_choices_to={"thirds__name": "Medico"},
        null=True,
        blank=True,
    )
    signed_obj=models.TextField(null=True,blank=True)  
    relationship_obj = models.CharField(max_length=2,choices=RELATIONSHIP_CHOICES,null=True, blank=True)
    observations = models.CharField(max_length=200,null=True, blank=True)    
    body= ArrayField(models.CharField(max_length=300), blank=True,  null=True)  
    body_side= ArrayField(models.CharField(max_length=300), blank=True, null=True)
    injuries = models.CharField(max_length=300,null=True, blank=True)    
    list_injuries =  models.CharField(max_length=500,null=True, blank=True)    
    service =models.ManyToManyField(Services, null=True, blank=True)
    total_services = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    policy=models.ForeignKey('Policy', on_delete=models.PROTECT, null=True, blank=True)
    
    imgcc = models.ImageField(upload_to='records/', null=True, blank=True)
    imgso= models.ImageField(upload_to='records/', null=True, blank=True)
    imgtp= models.ImageField(upload_to='records/', null=True, blank=True)
    imglc= models.ImageField(upload_to='records/', null=True, blank=True)
    imgco= models.ImageField(upload_to='records/', null=True, blank=True)
    imgic= models.ImageField(upload_to='records/', null=True, blank=True)
    
    class Meta:
        ordering = ['date_time']
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        

    def __str__(self): 
        return f"{self.id}"
    
class Values(models.Model):
    values=models.CharField(max_length=2,choices=VALUES_CHOICES)
    amount=models.DecimalField(max_digits=12, decimal_places=2, default=0)
    year_date=models.DateField(default=datetime(datetime.now().year, 1, 1)) 
    
    class Meta:
        ordering = ['values']
        verbose_name = 'Valor'
        verbose_name_plural = 'Valores'
    

    