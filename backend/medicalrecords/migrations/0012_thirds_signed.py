# Generated by Django 5.1.1 on 2024-11-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medicalrecords", "0011_alter_fees_policy_alter_fees_service_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="thirds",
            name="signed",
            field=models.TextField(blank=True, null=True),
        ),
    ]
