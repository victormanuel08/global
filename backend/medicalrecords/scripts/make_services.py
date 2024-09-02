from medicalrecords.models.specialities import *


services_to_create = [
    {'id': '1', 'code': 'OX', 'description': 'Oxigenacion', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '2', 'code': 'AS', 'description': 'Aspiracion', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '3', 'code': 'VE', 'description': 'Ventilacion', 'speciality_id':'56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '4', 'code': 'IN', 'description': 'Intubacion', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '5', 'code': 'RC', 'description': 'RCCP', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '6', 'code': 'DE', 'description': 'Desfibrilacion', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '7', 'code': 'MO', 'description': 'Monitoreo', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '8', 'code': 'SU', 'description': 'Sutura', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '9', 'code': 'VN', 'description': 'Vendas', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '10', 'code': 'IM', 'description': 'Inmovilizacion', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '11', 'code': 'CC', 'description': 'Collar Cervical', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '12', 'code': 'PA', 'description': 'Parto', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '13', 'code': 'AP', 'description': 'Asepsia', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '14', 'code': 'LI', 'description': 'Liquidos', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '15', 'code': 'ME', 'description': 'Medicación', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
    {'id': '16', 'code': 'OT', 'description': 'Otros', 'speciality_id': '56', 'amount_soat': '10000','amount_particular': '10000'},
]

# Creación de objetos Procedures
for services_data in services_to_create: # esto
    try:
        services = services.objects.create(**services_data)
        print("Created Servicios:", services)
    except Exception as e:
        print("Error creating Servicios:", e)
