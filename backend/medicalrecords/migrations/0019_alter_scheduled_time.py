# Generated by Django 5.0.6 on 2024-07-09 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0018_alter_scheduled_time_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduled',
            name='time',
            field=models.TimeField(default=datetime.time(14, 56, 6, 621229), verbose_name='Hora'),
        ),
    ]
