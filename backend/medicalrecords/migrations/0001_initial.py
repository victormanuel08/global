# Generated by Django 5.1 on 2024-08-26 21:23

import datetime
import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.IntegerField()),
                ('quota', models.IntegerField()),
                ('date', models.DateField()),
                ('overflow', models.IntegerField(default=0)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Disponibilidad',
                'verbose_name_plural': 'Disponibilidades',
                'ordering': ['third', 'date'],
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('municipality_dane_code', models.CharField(blank=True, max_length=10, null=True)),
                ('departament_dane_code', models.CharField(blank=True, max_length=10, null=True)),
                ('region', models.CharField(max_length=100)),
                ('departament', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Diagnoses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=300)),
                ('extra', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Diagnóstico',
                'verbose_name_plural': 'Diagnósticos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GeneralExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Examen General',
                'verbose_name_plural': 'Examen General',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Procedures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Procedimiento',
                'verbose_name_plural': 'Procedimientos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=300)),
                ('amount_soat', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount_particular', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Specialities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=300)),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='SystemsReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Revision de Sistemas',
                'verbose_name_plural': 'Revision de Sistemas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_values', models.CharField(choices=[('SE', 'SOAT'), ('SM', 'SALARIO MINIMO'), ('FO', 'FOSIGA-ECAT')], default='SE', max_length=2)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('year_date', models.DateField(default=datetime.datetime(2024, 1, 1, 0, 0))),
            ],
            options={
                'verbose_name': 'Valor',
                'verbose_name_plural': 'Valores',
                'ordering': ['type_values'],
            },
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('plate', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(choices=[('AM', 'AMBULANCIA'), ('AU', 'AUTOMOVIL'), ('MO', 'MOTO'), ('CA', 'CAMIONETA'), ('BU', 'BUS'), ('CA', 'CAMION'), ('OT', 'OTRO')], max_length=2)),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
                'ordering': ['brand'],
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('name', models.CharField(default='Contrato', max_length=100)),
                ('date_start', models.DateField(default=datetime.datetime(2024, 1, 1, 0, 0))),
                ('date_end', models.DateField(default=datetime.datetime(2024, 12, 31, 0, 0))),
                ('payment_model', models.CharField(choices=[('FF', 'FONDO FIJO'), ('EV', 'EVENTO')], default='SE', max_length=2)),
                ('type_police', models.CharField(choices=[('SE', 'SOAT'), ('AD', 'ADRES'), ('EP', 'EAPB'), ('PA', 'PARTICULAR'), ('EZ', 'ZONA SEGURA'), ('AR', 'ARL'), ('MP', 'MEDICINA PREPAGADA'), ('VI', 'VINCULADOS')], default='SE', max_length=2)),
                ('amount_total', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('amount_affection', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('template', models.BooleanField(default=False)),
                ('template_origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medicalrecords.policy')),
            ],
            options={
                'verbose_name': 'Poliza',
                'verbose_name_plural': 'Polizas',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medicalrecords.policy')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalrecords.services')),
                ('specialities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalrecords.specialities')),
            ],
            options={
                'verbose_name': 'Honorario',
                'verbose_name_plural': 'Honorarios',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reason_consultation', models.CharField(blank=True, max_length=100, null=True)),
                ('history', models.CharField(blank=True, max_length=100, null=True)),
                ('systems_review', models.CharField(blank=True, max_length=100, null=True)),
                ('general_exam', models.CharField(blank=True, max_length=100, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('signed', models.TextField(blank=True, null=True)),
                ('priority', models.CharField(blank=True, choices=[('W', 'Blanco'), ('R', 'Rojo'), ('Y', 'Amarillo'), ('G', 'Verde'), ('B', 'Negro')], max_length=6, null=True)),
                ('relationship', models.CharField(blank=True, choices=[('PA', 'PADRE'), ('MA', 'MADRE'), ('HO', 'HIJO'), ('HE', 'HERMAN@'), ('SO', 'SOBRIN@'), ('CO', 'CONYUGE'), ('PR', 'PRIM@'), ('AB', 'ABUEL@'), ('NI', 'NIET@'), ('TI', 'TI@'), ('SU', 'SUEGR@'), ('CU', 'CUÑAD@'), ('OT', 'OTRO')], max_length=2, null=True)),
                ('external_cause', models.CharField(blank=True, choices=[('GE', 'ENF GENERAL'), ('CA', 'ACCIDENTE COMUN'), ('TA', 'ACCIDENTE TRANSITO'), ('AG', 'LESION AGRESION'), ('AU', 'LESION AUTOINFLINGIDA'), ('CA', 'CATASTROFE'), ('LA', 'ACCIDENTE LABORAL'), ('RB', 'ACC RBICO U OFIDICO'), ('OT', 'OTRO')], max_length=2, null=True)),
                ('zone', models.CharField(blank=True, max_length=10, null=True)),
                ('ef_fc', models.CharField(blank=True, max_length=10, null=True)),
                ('ef_fr', models.CharField(blank=True, max_length=10, null=True)),
                ('ef_pa', models.CharField(blank=True, max_length=10, null=True)),
                ('ef_temp', models.CharField(blank=True, max_length=10, null=True)),
                ('glasgow_ro', models.CharField(blank=True, choices=[('4', 'ESPOTANEA'), ('3', 'A ESTIMULO VERBAL'), ('2', 'A ESTIMULO DOLOROSO'), ('1', 'NINGUNA')], max_length=10, null=True)),
                ('glasgow_rv', models.CharField(blank=True, choices=[('5', 'ORIENTADO'), ('4', 'CONFUSO'), ('3', 'PALABRAS INADECUADAS'), ('2', 'SONIDOS INADECUADOS'), ('1', 'NINGUNA')], max_length=10, null=True)),
                ('glasgow_rm', models.CharField(blank=True, choices=[('6', 'OBEDECE ORDENES'), ('5', 'LOCALIZA DOLOR'), ('4', 'FLEXION NORMAL'), ('3', 'FLEXION ANORMAL'), ('2', 'EXTENSION'), ('1', 'NINGUNA')], max_length=10, null=True)),
                ('procedures_others', models.CharField(blank=True, max_length=300, null=True)),
                ('half', models.CharField(blank=True, choices=[('TE', 'Telfonico'), ('RA', 'Padio'), ('PE', 'Personal'), ('OB', 'Observado')], max_length=2, null=True)),
                ('time_start', models.TimeField(blank=True, null=True)),
                ('time_end', models.TimeField(blank=True, null=True)),
                ('live', models.BooleanField(blank=True, null=True)),
                ('signed_driver', models.TextField(blank=True, null=True)),
                ('signed_recived', models.TextField(blank=True, null=True)),
                ('obj', models.BooleanField(blank=True, null=True)),
                ('value_obj', models.CharField(blank=True, max_length=200, null=True)),
                ('signed_obj', models.TextField(blank=True, null=True)),
                ('relationship_obj', models.CharField(blank=True, choices=[('PA', 'PADRE'), ('MA', 'MADRE'), ('HO', 'HIJO'), ('HE', 'HERMAN@'), ('SO', 'SOBRIN@'), ('CO', 'CONYUGE'), ('PR', 'PRIM@'), ('AB', 'ABUEL@'), ('NI', 'NIET@'), ('TI', 'TI@'), ('SU', 'SUEGR@'), ('CU', 'CUÑAD@'), ('OT', 'OTRO')], max_length=2, null=True)),
                ('observations', models.CharField(blank=True, max_length=200, null=True)),
                ('body', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), blank=True, null=True, size=None)),
                ('body_side', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=300), blank=True, null=True, size=None)),
                ('injuries', models.CharField(blank=True, max_length=300, null=True)),
                ('list_injuries', models.CharField(blank=True, max_length=500, null=True)),
                ('total_services', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('number_report', models.CharField(blank=True, max_length=100, null=True)),
                ('condition', models.CharField(blank=True, choices=[('CV', 'Conductor Vehiculo'), ('PV', 'Pasajero Vehiculo'), ('CM', 'Conductor Moto'), ('PM', 'Pasajero Moto'), ('PA', 'Peaton Mayor'), ('PN', 'Peaton Menor'), ('CC', 'Ciclista'), ('OT', 'Otro')], max_length=2, null=True)),
                ('imgcc', models.ImageField(blank=True, null=True, upload_to='records/')),
                ('imgso', models.ImageField(blank=True, null=True, upload_to='records/')),
                ('imgtp', models.ImageField(blank=True, null=True, upload_to='records/')),
                ('imglc', models.ImageField(blank=True, null=True, upload_to='records/')),
                ('imgco', models.ImageField(blank=True, null=True, upload_to='records/')),
                ('imgic', models.ImageField(blank=True, null=True, upload_to='records/')),
                ('latitude', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medicalrecords.cities')),
                ('diagnosis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='diagnosis', to='medicalrecords.diagnoses', verbose_name='Diagnostico')),
                ('diagnosis_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='diagnosis_1', to='medicalrecords.diagnoses', verbose_name='Primer Diagnostico')),
                ('diagnosis_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis_2', to='medicalrecords.diagnoses', verbose_name='Segundo Diagnostico')),
                ('diagnosis_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis_3', to='medicalrecords.diagnoses', verbose_name='Tercer Diagnostico')),
                ('policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medicalrecords.policy')),
                ('procedures', models.ManyToManyField(blank=True, to='medicalrecords.procedures')),
                ('types_general_exam', models.ManyToManyField(blank=True, to='medicalrecords.generalexam')),
                ('service', models.ManyToManyField(blank=True, null=True, to='medicalrecords.services')),
                ('types_systems_review', models.ManyToManyField(blank=True, to='medicalrecords.systemsreview')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
                'ordering': ['date_time'],
            },
        ),
        migrations.CreateModel(
            name='Records_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('signed', models.TextField(blank=True, null=True)),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Records', to='medicalrecords.records', verbose_name='Registro')),
            ],
            options={
                'verbose_name': 'Detalle de Registro',
                'verbose_name_plural': 'Detalle de Registros',
            },
        ),
        migrations.AddField(
            model_name='services',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicalrecords.specialities'),
        ),
        migrations.CreateModel(
            name='Scheduled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha solicitada')),
                ('time', models.TimeField(verbose_name='Hora')),
                ('confirmed', models.BooleanField(blank=True, null=True)),
                ('insurance', models.BooleanField(blank=True, null=True)),
                ('date_origin', models.DateField(default='1999-01-01')),
                ('fee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fees', to='medicalrecords.fees', verbose_name='Tarifa')),
                ('policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sheduled_policy', to='medicalrecords.policy', verbose_name='Poliza')),
                ('record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='records', to='medicalrecords.records', verbose_name='Historia')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='services', to='medicalrecords.services', verbose_name='Servicio')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specialities', to='medicalrecords.specialities', verbose_name='Especialidad')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'ordering': ['date', 'time'],
            },
        ),
        migrations.CreateModel(
            name='Thirds',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_document', models.CharField(blank=True, choices=[('CC', 'Cedula de Ciudadania'), ('CE', 'Cedula de Extranjeria'), ('PA', 'Pasaporte'), ('RC', 'Registro Civil'), ('TI', 'Tarjeta de Identidad'), ('NU', 'Numero Unico de Identificacion'), ('PE', 'Permiso Especial de Permanencia'), ('AS', 'Adulto sin Identificacion'), ('NI', 'Nit')], default='CC', max_length=2, null=True)),
                ('nit', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('second_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('second_last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('year_old', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], max_length=2, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, choices=[('P', 'Paciente / Otros'), ('M', 'Medico'), ('E', 'Entidad'), ('C', 'Clinica')], max_length=2, null=True)),
                ('maternity_pregnancy', models.CharField(blank=True, choices=[('NI', 'Ninguno'), ('PT', 'Primer Trimestre'), ('ST', 'Segundo Trimestre'), ('TT', 'Tercer Trimestre'), ('PU', 'Puérperio')], max_length=2, null=True)),
                ('maternity_breasfeeding', models.CharField(blank=True, choices=[('NI', 'Ninguno'), ('UM', 'Menos de 1 mes'), ('TM', '1 a 3 meses'), ('SM', '3 a 6 meses'), ('MM', 'Mas de 6 meses'), ('UA', 'Mas de 1 año')], max_length=2, null=True)),
                ('maternity_breasfeeding_extend', models.CharField(blank=True, choices=[('NI', 'Nunca'), ('UM', 'Menos de 1 Mes'), ('TM', '1 a 3 meses'), ('SM', '3 a 6 meses')], max_length=2, null=True)),
                ('maternity_breasfeeding_complementary', models.CharField(blank=True, choices=[('NI', 'Nunca'), ('UM', 'Menos de 1 Mes'), ('TM', '1 a 3 meses'), ('SM', '3 a 6 meses')], max_length=2, null=True)),
                ('maternity_violence', models.CharField(blank=True, choices=[('NI', 'Ninguno'), ('MA', 'Mina ANtipersona'), ('DM', 'Desmovilizado'), ('RS', 'Reinsertado'), ('IN', 'Intrafamiliar')], max_length=2, null=True)),
                ('ethnicity', models.CharField(blank=True, choices=[('N', 'Ninguno'), ('I', 'Indigena'), ('A', 'AfroColombiano'), ('G', 'ROM - Gitano'), ('R', 'Raizal')], max_length=2, null=True)),
                ('blood_type', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True)),
                ('status', models.CharField(blank=True, choices=[('S', 'Soltero'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viudo'), ('U', 'Union Libre')], max_length=2, null=True)),
                ('occupation', models.CharField(blank=True, choices=[('E', 'Empleado'), ('I', 'Independiente'), ('D', 'Desempleado'), ('P', 'Pensionado'), ('E', 'Estudiante'), ('H', 'Hogar')], max_length=2, null=True)),
                ('zone', models.CharField(blank=True, choices=[('U', 'Urbana'), ('R', 'Rural')], max_length=2, null=True)),
                ('allergies', models.CharField(blank=True, max_length=200, null=True)),
                ('pathologies', models.CharField(blank=True, max_length=200, null=True)),
                ('medications', models.CharField(blank=True, max_length=200, null=True)),
                ('liquids_foods', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medicalrecords.cities')),
                ('city_birth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='city_birth', to='medicalrecords.cities')),
                ('policys', models.ManyToManyField(blank=True, null=True, to='medicalrecords.policy')),
                ('speciality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medicalrecords.specialities')),
            ],
            options={
                'verbose_name': 'Tercero',
                'verbose_name_plural': 'Terceros',
                'ordering': ['nit'],
            },
        ),
    ]
