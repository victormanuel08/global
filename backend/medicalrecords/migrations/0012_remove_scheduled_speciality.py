# Generated by Django 5.0.6 on 2024-07-04 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0011_alter_scheduled_third_medic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduled',
            name='speciality',
        ),
    ]
