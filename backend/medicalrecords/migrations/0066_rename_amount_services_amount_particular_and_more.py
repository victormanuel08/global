# Generated by Django 5.0.6 on 2024-08-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalrecords', '0065_alter_values_values'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='amount',
            new_name='amount_particular',
        ),
        migrations.RemoveField(
            model_name='records',
            name='fee',
        ),
        migrations.AddField(
            model_name='policy',
            name='amount_affection',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='records',
            name='total_services',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='services',
            name='amount_soat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='payment_model',
            field=models.CharField(choices=[('FF', 'FONDO FIJO'), ('EV', 'EVENTO')], default='SE', max_length=2),
        ),
        migrations.RemoveField(
            model_name='records',
            name='service',
        ),
        migrations.AlterField(
            model_name='values',
            name='values',
            field=models.CharField(choices=[('SE', 'SOAT'), ('FO', 'FOSIGA-ECAT'), ('SM', 'SALARIO MINIMO')], max_length=2),
        ),
        migrations.AddField(
            model_name='records',
            name='service',
            field=models.ManyToManyField(blank=True, null=True, to='medicalrecords.services'),
        ),
    ]
