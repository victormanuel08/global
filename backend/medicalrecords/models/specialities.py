from django.db import models

class Specialities(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    description = models.TextField(max_length=300)    
    
    class Meta:
        db_table = 'speciality'
        verbose_name = 'speciality'
        verbose_name_plural = 'speciality'
        
    def __str__(self):
        return self.name
    