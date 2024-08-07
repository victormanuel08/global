# Generated by Django 5.0.6 on 2024-07-16 23:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0033_rename_records_details_records_records_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='records_details',
        ),
        migrations.AddField(
            model_name='records_details',
            name='record',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.PROTECT, related_name='Records', to='medicalrecords.records', verbose_name='Registro'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='records_details',
            name='observation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='records_details',
            name='signed',
            field=models.TextField(),
        ),
    ]
