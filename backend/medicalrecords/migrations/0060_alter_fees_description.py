# Generated by Django 5.0.6 on 2024-08-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0059_scheduled_fee_scheduled_policy_scheduled_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]