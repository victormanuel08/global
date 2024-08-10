# Generated by Django 5.0.6 on 2024-08-08 19:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0068_alter_thirds_policys_alter_values_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='list_injuries',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='values',
            name='values',
            field=models.CharField(choices=[('SM', 'SALARIO MINIMO'), ('SE', 'SOAT'), ('FO', 'FOSIGA-ECAT')], max_length=2),
        ),
    ]
