# Generated by Django 5.0.6 on 2024-07-25 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0043_alter_records_time_end_alter_records_time_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='signed_profesional_send',
        ),
        migrations.RemoveField(
            model_name='records',
            name='third_relationship',
        ),
        migrations.AddField(
            model_name='records',
            name='third_medic_clinic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='thirds_medic_clinic', to='medicalrecords.thirds', verbose_name='Medico'),
        ),
    ]
