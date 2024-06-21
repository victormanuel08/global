from django.db import models

class Diagnoses(models.Model):
    id = models.AutoField(primary_key=True)
    code= models.CharField(max_length=20)
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    extra = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'diagnoses'
        verbose_name = 'diagnoses'
        verbose_name_plural = 'diagnoses'

    def __str__(self):
        return self.name
    