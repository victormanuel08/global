# Generated by Django 5.0.6 on 2024-07-05 14:55

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0015_alter_scheduled_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduled',
            name='third_medic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='scheduled_medics', to='medicalrecords.thirds', verbose_name='Tercero Medico'),
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='time',
            field=models.TimeField(default=datetime.time(9, 55, 29, 512338), verbose_name='Hora'),
        ),
    ]
