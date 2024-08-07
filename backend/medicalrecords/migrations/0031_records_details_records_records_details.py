# Generated by Django 5.0.6 on 2024-07-13 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0030_scheduled_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.CharField(blank=True, max_length=100, null=True)),
                ('systems_review', models.CharField(blank=True, max_length=100, null=True)),
                ('general_exam', models.CharField(blank=True, max_length=100, null=True)),
                ('observation', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Detalle de Registro',
                'verbose_name_plural': 'Detalle de Registros',
            },
        ),
        migrations.AddField(
            model_name='records',
            name='Records_details',
            field=models.ManyToManyField(to='medicalrecords.records_details'),
        ),
    ]
