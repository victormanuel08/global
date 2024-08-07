# Generated by Django 5.0.6 on 2024-08-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0061_values_services_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirds',
            name='policys',
            field=models.ManyToManyField(to='medicalrecords.policy'),
        ),
        migrations.AlterField(
            model_name='records',
            name='priority',
            field=models.CharField(blank=True, choices=[('W', 'Blanco'), ('R', 'Rojo'), ('Y', 'Amarillo'), ('G', 'Verde'), ('B', 'Negro')], max_length=6, null=True),
        ),
    ]
