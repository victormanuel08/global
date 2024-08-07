# Generated by Django 5.0.6 on 2024-08-06 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0063_policy_template_alter_policy_type_police_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fees',
            name='code',
        ),
        migrations.AddField(
            model_name='policy',
            name='template_origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medicalrecords.policy'),
        ),
        migrations.AlterField(
            model_name='values',
            name='values',
            field=models.CharField(choices=[('FO', 'FOSIGA-ECAT'), ('SE', 'SOAT'), ('SM', 'SALARIO MINIMO')], max_length=2),
        ),
    ]
