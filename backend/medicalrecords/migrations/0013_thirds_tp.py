# Generated by Django 5.1.1 on 2024-11-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medicalrecords", "0012_thirds_signed"),
    ]

    operations = [
        migrations.AddField(
            model_name="thirds",
            name="tp",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
