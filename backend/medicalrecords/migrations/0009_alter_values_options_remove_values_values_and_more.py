# Generated by Django 5.1 on 2024-08-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0008_records_address_records_latitude_records_longitude_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='values',
            options={'ordering': ['type_values'], 'verbose_name': 'Valor', 'verbose_name_plural': 'Valores'},
        ),
        migrations.RemoveField(
            model_name='values',
            name='values',
        ),
        migrations.AddField(
            model_name='values',
            name='type_values',
            field=models.CharField(choices=[('SM', 'SALARIO MINIMO'), ('FO', 'FOSIGA-ECAT'), ('SE', 'SOAT')], default='SE', max_length=2),
        ),
    ]
