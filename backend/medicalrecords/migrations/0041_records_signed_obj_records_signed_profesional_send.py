# Generated by Django 5.0.6 on 2024-07-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0040_alter_records_observations'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='signed_obj',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='records',
            name='signed_profesional_send',
            field=models.TextField(blank=True, null=True),
        ),
    ]
