# Generated by Django 5.0.6 on 2024-07-09 13:45

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0017_thirds_user_alter_scheduled_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduled',
            name='time',
            field=models.TimeField(default=datetime.time(8, 45, 31, 719943), verbose_name='Hora'),
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.IntegerField()),
                ('quota', models.IntegerField()),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('third', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='medicalrecords.thirds')),
            ],
            options={
                'verbose_name': 'Disponibilidad',
                'verbose_name_plural': 'Disponibilidades',
                'ordering': ['third'],
            },
        ),
    ]
