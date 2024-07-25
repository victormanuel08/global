# Generated by Django 5.0.6 on 2024-07-24 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0038_procedures_rename_allergies_records_live_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='procedures_others',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='records',
            name='procedures',
            field=models.ManyToManyField(blank=True, null=True, to='medicalrecords.procedures'),
        ),
        migrations.AlterField(
            model_name='records',
            name='types_general_exam',
            field=models.ManyToManyField(blank=True, null=True, to='medicalrecords.generalexam'),
        ),
        migrations.AlterField(
            model_name='records',
            name='types_systems_review',
            field=models.ManyToManyField(blank=True, null=True, to='medicalrecords.systemsreview'),
        ),
        migrations.AlterField(
            model_name='thirds',
            name='type',
            field=models.CharField(blank=True, choices=[('P', 'Paciente'), ('M', 'Medico'), ('E', 'Entidad'), ('C', 'Clinica')], max_length=2, null=True),
        ),
    ]
