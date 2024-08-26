# Generated by Django 5.1 on 2024-08-24 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0002_thirds_vehicle_alter_thirds_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medicalrecords.vehicles'),
        ),
        migrations.AlterField(
            model_name='values',
            name='type_values',
            field=models.CharField(choices=[('FO', 'FOSIGA-ECAT'), ('SM', 'SALARIO MINIMO'), ('SE', 'SOAT')], default='SE', max_length=2),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='vehicle_type',
            field=models.CharField(choices=[('AM', 'AMBULANCIA'), ('AU', 'AUTOMOVIL'), ('MO', 'MOTO'), ('CA', 'CAMIONETA'), ('BU', 'BUS'), ('CA', 'CAMION'), ('OT', 'OTRO')], max_length=2),
        ),
    ]