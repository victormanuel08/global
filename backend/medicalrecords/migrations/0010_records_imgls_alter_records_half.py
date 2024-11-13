# Generated by Django 5.1.1 on 2024-11-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medicalrecords", "0009_records_imghd_records_imghdr"),
    ]

    operations = [
        migrations.AddField(
            model_name="records",
            name="imgls",
            field=models.ImageField(blank=True, null=True, upload_to="records/"),
        ),
        migrations.AlterField(
            model_name="records",
            name="half",
            field=models.CharField(
                blank=True,
                choices=[
                    ("TE", "Telfonico"),
                    ("RA", "Radio"),
                    ("PE", "Personal"),
                    ("OB", "Observado"),
                ],
                max_length=2,
                null=True,
            ),
        ),
    ]
