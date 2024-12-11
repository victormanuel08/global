# Generated by Django 5.1.1 on 2024-12-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medicalrecords", "0015_alter_medicamentsrecords_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="thirds",
            name="profesion",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="records",
            name="descript_procedures",
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name="records",
            name="reason_consultation",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="thirds",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("P", "Paciente"),
                    ("M", "Medico"),
                    ("O", "Conductor"),
                    ("E", "Entidad"),
                    ("C", "Clinica"),
                ],
                max_length=2,
                null=True,
            ),
        ),
    ]
