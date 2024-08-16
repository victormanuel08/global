# Generated by Django 5.1 on 2024-08-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0006_records_number_report_alter_values_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='condition',
            field=models.CharField(blank=True, choices=[('CV', 'Conductor Vehiculo'), ('PV', 'Pasajero Vehiculo'), ('CM', 'Conductor Moto'), ('PM', 'Pasajero Moto'), ('PA', 'Peaton Mayor'), ('PN', 'Peaton Menor'), ('CC', 'Ciclista'), ('OT', 'Otro')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='values',
            name='values',
            field=models.CharField(choices=[('FO', 'FOSIGA-ECAT'), ('SM', 'SALARIO MINIMO'), ('SE', 'SOAT')], max_length=2),
        ),
    ]
