# Generated by Django 5.1 on 2024-09-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0006_records_descript_procedures_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='signed_dactilar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='values',
            name='type_values',
            field=models.CharField(choices=[('SE', 'SOAT'), ('FO', 'FOSIGA-ECAT'), ('SM', 'SALARIO MINIMO'), ('EO', 'EMAIL ORIGEN (Gmail)'), ('ED', 'EMAIL DESTINO (Gmail)'), ('EP', 'CLAVE APP EMAIL ORIGEN (Gmail)')], max_length=2),
        ),
    ]
