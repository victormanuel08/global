from medicalrecords.models import SystemsReview, GeneralExam

systemsreview_to_create = [
    {'code': 'RE', 'name': 'Respiratorio'},
    {'code': 'NP', 'name': 'NeuroPsiquiatrico'},
    {'code': 'OS', 'name': 'Organos de los Sentidos'},
    {'code': 'CA', 'name': 'Cardiovascular'},
    {'code': 'CP', 'name': 'Cardiopulmonar'},
    {'code': 'NE', 'name': 'Neurológico'},
    {'code': 'CI', 'name': 'Circulatorio'},
    {'code': 'HL', 'name': 'Hematopoyetico y Linfatico'},
    {'code': 'EN', 'name': 'Endocrinologo'},
    {'code': 'GA', 'name': 'Gastrointestinal'},
    {'code': 'RE', 'name': 'Renal'},
    {'code': 'GU', 'name': 'GenitoUrinario'},
    {'code': 'PF', 'name': 'Piel y Faneras'},
    {'code': 'OM', 'name': 'OsteoMuscular'},
    {'code': 'OT', 'name': 'Otros'}
]

generalexam_to_create = [
    {'code': 'OI', 'name': 'Oidos'},
    {'code': 'NA', 'name': 'Nariz'},
    {'code': 'BO', 'name': 'Boca'},
    {'code': 'CU', 'name': 'Cuello'},
    {'code': 'TO', 'name': 'Torax'},
    {'code': 'AB', 'name': 'Abdomen'},
    {'code': 'GU', 'name': 'GenitoUrinario'},
    {'code': 'OS', 'name': 'OsteoArticular'},
    {'code': 'SN', 'name': 'Sistema Nervioso'},
    {'code': 'PF', 'name': 'Piel y Faneras'},
    {'code': 'ME', 'name': 'Musculo Esqueletico'},
    {'code': 'NM', 'name': 'Neurologia Esfera Mental'},
    {'code': 'CP', 'name': 'Cardio Pulmonar'}
]



# Creación de objetos GeneralExam
for generalexam_data in generalexam_to_create:
    try:
        generalexam = GeneralExam.objects.create(**generalexam_data)
        print("Created GeneralExam:", generalexam)
    except Exception as e:
        print("Error creating GeneralExam:", e)

# python3 manage.py shell < backend/medicalrecords/scripts/make_records.py

for systemsreview_data in systemsreview_to_create:
    try:
        systemsreview = SystemsReview.objects.create(**systemsreview_data)
        print("Created SystemsReview:", systemsreview)
    except Exception as e:
        print("Error creating SystemsReview:", e)