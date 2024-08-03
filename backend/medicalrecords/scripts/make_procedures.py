from medicalrecords.models import *

procedures_to_create = [
    {'code': 'OX', 'name': 'Oxigenacion'},
    {'code': 'AS', 'name': 'Aspiracion'},
    {'code': 'VE', 'name': 'Ventilacion'},
    {'code': 'IN', 'name': 'Intubacion'},
    {'code': 'RC', 'name': 'RCCP'},
    {'code': 'DE', 'name': 'Desfibrilacion'},
    {'code': 'MO', 'name': 'Monitoreo'},
    {'code': 'SU', 'name': 'Sutura'},
    {'code': 'VE', 'name': 'Vendas'},
    {'code': 'IN', 'name': 'Inmovilizacion'},
    {'code': 'CC', 'name': 'Collar Cervical'},
    {'code': 'PA', 'name': 'Parto'},
    {'code': 'AS', 'name': 'Asepsia'},
    {'code': 'LI', 'name': 'Liquidos'},
    {'code': 'ME', 'name': 'Medicación'},
    {'code': 'OT', 'name': 'Otros'}
]

# Creación de objetos Procedures
for procedures_data in procedures_to_create:
    try:
        procedures = Procedures.objects.create(**procedures_data)
        print("Created Procedures:", procedures)
    except Exception as e:
        print("Error creating Procedures:", e)
