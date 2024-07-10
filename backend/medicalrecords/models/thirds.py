from django.db import models
from .specialities import Specialities
from datetime import datetime

ETNIAS_CHOICES = (
    ('N', 'Ninguno'),
    ('I', 'Indigena'),
    ('A', 'AfroColombiano'),
    ('G', 'ROM - Gitano'),
    ('R', 'Raizal'),       
)

SEX_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otros')
)   

TYPE_CHOICES = (
    ('P', 'Paciente'),
    ('M', 'Medico')
)

BLOOD_CHOICES = (
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
)

MATERNITY_PREGNANCY_CHOICES = (
    ('NI', 'Ninguno'),
    ('PT', 'Primer Trimestre'),
    ('ST', 'Segundo Trimestre'),
    ('TT', 'Tercer Trimestre'),
    ('PU', 'Puérperio')
)    

MATERNITY_BREASFEEDING_CHOICES = (
    ('0', 'Ninguno'),
    ('1', 'Menos de 1 mes'),
    ('2', '1 a 3 meses'),
    ('3', '3 a 6 meses'),
    ('4', 'Mas de 6 meses'),
    ('5', 'Mas de 1 año')
)

MATERNITY_BREASFEEDING_EXTEND_CHOICES = (
    ('0', 'Nunca'),
    ('1', 'Menos de 1 Mes'),
    ('2', '1 a 3 meses'),
    ('3', '3 a 6 meses')
)

MATERNITY_BREASFEEDING_COMPLEMENTARY_CHOICES = (
    ('0', 'Nunca'),
    ('1', 'Menos de 1 Mes'),
    ('2', '1 a 3 meses'),
    ('3', '3 a 6 meses')
)

MATERNITY_VIOLANCE_CHOICES = (
    ('N', 'Ninguno'),
    ('M', 'Mina ANtipersona'),
    ('D', 'Desmovilizado'),
    ('R', 'Reinsertado'),
    ('I', 'Intrafamiliar')
)
    
# Create your models here.
class Thirds(models.Model):
    id = models.AutoField(primary_key=True)
    nit= models.CharField(max_length=100)    
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    second_last_name = models.CharField(max_length=100)
    date_birth= models.DateField(null=True, blank=True)
    year_old= models.IntegerField(null=True, blank=True)
    sex= models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    zone= models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, null=True, blank=True)
    speciality=models.ForeignKey(Specialities, on_delete=models.PROTECT, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    city_birth = models.CharField(max_length=100, null=True, blank=True)
    maternity_pregnancy = models.CharField(max_length=2, choices=MATERNITY_PREGNANCY_CHOICES, null=True, blank=True)
    maternity_breasfeeding = models.CharField(max_length=1, choices=MATERNITY_BREASFEEDING_CHOICES, null=True, blank=True)
    maternity_breasfeeding_extend = models.CharField(max_length=1, choices=MATERNITY_BREASFEEDING_EXTEND_CHOICES, null=True, blank=True)
    maternity_breasfeeding_complementary = models.CharField(max_length=1, choices=MATERNITY_BREASFEEDING_COMPLEMENTARY_CHOICES, null=True, blank=True)
    maternity_violence = models.CharField(max_length=1, choices=MATERNITY_VIOLANCE_CHOICES, null=True, blank=True)
    ethnicity = models.CharField(max_length=1, choices=ETNIAS_CHOICES, null=True, blank=True)
    blood_type= models.CharField(max_length=3, choices=BLOOD_CHOICES, null=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        today = datetime.now().date()
        birth_date = self.date_birth

        if birth_date:            
            age = today.year - birth_date.year - int((today.month, today.day) < (birth_date.month, birth_date.day))
            self.year_old = age
        else:            
            self.year_old = None  
        super(Thirds, self).save(*args, **kwargs)
    
    class Meta:       
        ordering = ['nit']
        verbose_name = 'Tercero'
        verbose_name_plural = 'Terceros'

    def __str__(self):
        return self.nit
    

class Availability(models.Model):
    id = models.AutoField(primary_key=True)
    third = models.ForeignKey(Thirds, on_delete=models.PROTECT)
    time = models.IntegerField()
    quota = models.IntegerField()
    date = models.DateField()
    overflow = models.BooleanField(default=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:       
        ordering = ['third','date']
        verbose_name = 'Disponibilidad'
        verbose_name_plural = 'Disponibilidades'

    def __str__(self):
        return self.third.name