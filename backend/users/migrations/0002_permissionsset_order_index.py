# Generated by Django 5.1 on 2024-08-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permissionsset',
            name='order_index',
            field=models.IntegerField(default=0),
        ),
    ]
