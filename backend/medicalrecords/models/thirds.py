from django.db import models

ETNIAS_CHOICES = (
    ('N', 'Ninguno'),
    ('I', 'Indigena'),
    ('A', 'AfroColombiano'),
    ('G', 'ROM - Gitano'),
    ('R', 'Raizal'),   
    # Agrega más opciones según tus necesidades
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
    date_birth= models.DateField()
    year_old= models.IntegerField()
    sex= models.CharField(max_length=1, choices=TYPE_CHOICES)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zone= models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    speciality=models.ForeignKey('Specialties', on_delete=models.PROTECT)
    city = models.CharField(max_length=100)
    city_birth = models.CharField(max_length=100)
    maternity_pregnancy = models.CharField(max_length=2, choices=MATERNITY_PREGNANCY_CHOICES)
    maternity_breasfeeding = models.CharField(max_length=1, choices=MATERNITY_BREASFEEDING_CHOICES)
    maternity_breasfeeding_extend = models.CharField(max_length=1, choices=MATERNITY_BREASFEEDING_EXTEND_CHOICES)
    maternity_breasfeeding_complementary = models.CharField(max_length=1, choices=MATERNITY_BREASFEEDING_COMPLEMENTARY_CHOICES)
    maternity_violence = models.CharField(max_length=1, choices=MATERNITY_VIOLANCE_CHOICES)
    ethnicity = models.CharField(max_length=1, choices=ETNIAS_CHOICES)
    blood_type= models.CharField(max_length=2, choices=BLOOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'thirds'
        verbose_name = 'thirds'
        verbose_name_plural = 'thirds'

    def __str__(self):
        return self.name