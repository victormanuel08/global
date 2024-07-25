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
    ('M', 'Medico'),
    ('E', 'Entidad'),
    ('C', 'Clinica')
)

TYPE_DOCUMENT_CHOICES = (
    ('CC', 'Cedula de Ciudadania'),
    ('CE', 'Cedula de Extranjeria'),
    ('PA', 'Pasaporte'),
    ('RC', 'Registro Civil'),
    ('TI', 'Tarjeta de Identidad'),
    ('NU', 'Numero Unico de Identificacion'),
    ('PE', 'Permiso Especial de Permanencia'),
    ('AS', 'Adulto sin Identificacion'),
    ('NI', 'Nit')
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
    ('NI', 'Ninguno'),
    ('UM', 'Menos de 1 mes'),
    ('TM', '1 a 3 meses'),
    ('SM', '3 a 6 meses'),
    ('MM', 'Mas de 6 meses'),
    ('UA', 'Mas de 1 año')
)

MATERNITY_BREASFEEDING_EXTEND_CHOICES = (
    ('NI', 'Nunca'),
    ('UM', 'Menos de 1 Mes'),
    ('TM', '1 a 3 meses'),
    ('SM', '3 a 6 meses')
)

MATERNITY_BREASFEEDING_COMPLEMENTARY_CHOICES = (
    ('NI', 'Nunca'),
    ('UM', 'Menos de 1 Mes'),
    ('TM', '1 a 3 meses'),
    ('SM', '3 a 6 meses')
)

MATERNITY_VIOLANCE_CHOICES = (
    ('NI', 'Ninguno'),
    ('MA', 'Mina ANtipersona'),
    ('DM', 'Desmovilizado'),
    ('RS', 'Reinsertado'),
    ('IN', 'Intrafamiliar')
)

STATUS_CHOICES = (
    ('S', 'Soltero'),
    ('C', 'Casado'),
    ('D', 'Divorciado'),
    ('V', 'Viudo'),
    ('U', 'Union Libre')
)

OCCUPATION_CHOICES = (
    ('E', 'Empleado'),
    ('I', 'Independiente'),
    ('D', 'Desempleado'),
    ('P', 'Pensionado'),
    ('E', 'Estudiante'),
    ('H', 'Hogar')
)

ZONE_CHOICES = (
    ('U', 'Urbana'),
    ('R', 'Rural')
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
    sex= models.CharField(max_length=2, choices=SEX_CHOICES, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    zone= models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, null=True, blank=True)
    speciality=models.ForeignKey(Specialities, on_delete=models.PROTECT, null=True, blank=True)
    city = models.ForeignKey('Cities', on_delete=models.PROTECT, null=True, blank=True)
    city_birth = models.ForeignKey('Cities', on_delete=models.PROTECT, null=True, blank=True, related_name='city_birth')
    maternity_pregnancy = models.CharField(max_length=2, choices=MATERNITY_PREGNANCY_CHOICES, null=True, blank=True)
    maternity_breasfeeding = models.CharField(max_length=2, choices=MATERNITY_BREASFEEDING_CHOICES, null=True, blank=True)
    maternity_breasfeeding_extend = models.CharField(max_length=2, choices=MATERNITY_BREASFEEDING_EXTEND_CHOICES, null=True, blank=True)
    maternity_breasfeeding_complementary = models.CharField(max_length=2, choices=MATERNITY_BREASFEEDING_COMPLEMENTARY_CHOICES, null=True, blank=True)
    maternity_violence = models.CharField(max_length=2, choices=MATERNITY_VIOLANCE_CHOICES, null=True, blank=True)
    ethnicity = models.CharField(max_length=2, choices=ETNIAS_CHOICES, null=True, blank=True)
    blood_type= models.CharField(max_length=3, choices=BLOOD_CHOICES, null=True, blank=True)
    status= models.CharField(max_length=2, choices=STATUS_CHOICES, null=True, blank=True)
    occupation = models.CharField(max_length=2, choices=OCCUPATION_CHOICES, null=True, blank=True)
    zone = models.CharField(max_length=2, choices=ZONE_CHOICES, null=True, blank=True)
    allergies = models.CharField(max_length=200, null=True, blank=True)
    pathologies = models.CharField(max_length=200, null=True, blank=True)
    medications = models.CharField(max_length=200, null=True, blank=True)
    liquids_foods = models.CharField(max_length=200, null=True, blank=True)    
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
    overflow = models.IntegerField(default=0)
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