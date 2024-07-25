from django.db import models

PRIORITY_CHOICES = (
    ('W', 'White'),
    ('R', 'Red'),
    ('Y', 'Yellow'),
    ('G', 'Green'),
    ('B', 'Black'),
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
    ('CA', 'Cabeza'),
    ('CU', 'Cuello'),
    ('TO', 'Torax'),
    ('DO', 'Dorso'),
    ('AB', 'Abdomen'),
    ('PE', 'Pelvis/Perine'),
    ('MI', 'Miembro Inferior'),
    ('SU', 'Miembro Superior'),
)

BODY_PART_SIDE_CHOICES = (
    ('GL', 'Glutea'),
    ('AM', 'Anterior Muslo'),
    ('PM', 'Posterior Muslo'),
    ('AR', 'Anterior Rodilla'),
    ('PR', 'Posterior Rodilla'),
    ('AP', 'Anterior Pierna'),
    ('PP', 'Posterior Pierna'),
    ('TA', 'Tobillo anterior'),
    ('TP', 'Tobullo posterior'),
    ('PI', 'Pie'),
)   
    

class Procedures(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Procedimiento'
        verbose_name_plural = 'Procedimientos'
        
    def __str__(self):
        return self.name    

class Policy(models.Model):    
    number= models.IntegerField()
    third_entity = models.ForeignKey(
        'Thirds',
        on_delete=models.PROTECT,
        verbose_name="Entidad",
        related_name="thirds_policy_entity",
        #limit_choices_to={"thirds__name": "Entidad"},
    )
    brand = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=2,choices=VEHICLE_TYPE_CHOICES)
    
    class Meta:
        ordering = ['number']
        verbose_name = 'Poliza'
        verbose_name_plural = 'Polizas'
        
    def __str__(self):
        return self.number

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
    signed_obj=models.TextField(null=True,blank=True)  
    relationship_obj = models.CharField(max_length=2,choices=RELATIONSHIP_CHOICES,null=True, blank=True)
    observations = models.CharField(max_length=200,null=True, blank=True)     
    
    
    
    class Meta:
        ordering = ['date_time']
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        
    def __str__(self):
        return self.diagnosis.name
    