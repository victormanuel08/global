# Generated by Django 5.0.6 on 2024-07-10 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0022_alter_scheduled_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'ordering': ['third', 'date'], 'verbose_name': 'Disponibilidad', 'verbose_name_plural': 'Disponibilidades'},
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='time',
            field=models.TimeField(default=datetime.time(8, 5, 49, 355975), verbose_name='Hora'),
        ),
    ]
