from django.db import models

SYSTEMS_REVIEW_CHOICES = (
    ('RE', 'Respiratorio'),
    ('NP', 'NeuroPsiquiatrico'),
    ('OS', 'Organos de los Sentidos'),
    ('CA', 'Cardiovascular'),
    ('CP', 'Cardiopulmonar'),
    ('NE', 'Neurológico'),
    ('CI', 'Circulatorio'),
    ('HL', 'Hematopoyetico y Linfatico'),
    ('EN', 'Endocrinologo'),
    ('GA', 'Gastrointestinal'),
    ('RE', 'Renal'),
    ('GU', 'GenitoUrinario'),
    ('PF', 'Piel y Faneras'),
    ('OM', 'OsteoMuscular'),
    ('OT', 'Otros')   
)

GENERAL_EXAM_CHOICES = (
    ('OI', 'Oidos'),
    ('NA', 'Nariz'),
    ('BO', 'Boca'),
    ('CU', 'Cuello'),
    ('TO', 'Torax'),
    ('AB', 'Abdomen'),
    ('GU', 'GenitoUrinario'),
    ('OS', 'OsteoArticular'),
    ('SN', 'Sistema Nervioso'),
    ('PF', 'Piel y Faneras'),
    ('ME', 'Musculo Esqueletico'),
    ('NM', 'Neurologia Esfera Mental'),
    ('CP', 'Cardio Pulmonar')   
)

class Records(models.model):
    id = models.AutoField(primary_key=True)
    third_id = models.ForeignKey('Thirds', on_delete=models.PROTECT)
    reason_consultation = models.CharField(max_length=100)
    history = models.CharField(max_length=100)    
    systems_review = models.CharField(max_length=100)    
    general_exam = models.CharField(max_length=100)    
    types_systems_review = models.ManyToManyField(choices=SYSTEMS_REVIEW_CHOICES)
    types_general_exam = models.ManyToManyField(choices=GENERAL_EXAM_CHOICES)
    allergies = models.BooleanField()
    third_doctor_id = models.ForeignKey('Thirds', on_delete=models.PROTECT)       
    date_time = models.DateTimeField(auto_now_add=True)   
    diagnosis = models.ForeignKey('Diagnosis', on_delete=models.PROTECT) 
    diagnosis_1 = models.ForeignKey('Diagnosis', on_delete=models.PROTECT)
    diagnosis_2 = models.ForeignKey('Diagnosis', on_delete=models.PROTECT)
    diagnosis_3 = models.ForeignKey('Diagnosis', on_delete=models.PROTECT)
    
    class Meta:
        db_table = 'records'
        verbose_name = 'records'
        verbose_name_plural = 'records'
        
    def __str__(self):
        return self.reason_consultation
    