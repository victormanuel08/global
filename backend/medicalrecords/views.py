from .models import *
from .serializers import *
from .models import Cities, Diagnoses, Records, Specialities, Thirds, GeneralExam, SystemsReview, Scheduled
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

    
class CityViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer
    search_fields = ['name']

class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnoses.objects.all()
    serializer_class = DiagnosisSerializer
    search_fields = ['name', 'code', 'description', 'extra']
    
class RecordViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    serializer_class = RecordSerializer
    search_fields = ['reason_consultation','third_patient__nit','third_patient__name','third_patient__second_name','third_patient__last_name','third_patient__second_last_name','third_medic__nit','third_medic__name','third_medic__second_name','third_medic__last_name','third_medic__second_last_name','diagnosis__name','diagnosis_1__name',"history", "systems_review", "general_exam",  "allergies", "date_time"]

class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Specialities.objects.all()
    serializer_class = SpecialitySerializer
    search_fields = ['code','description']

class ThirdViewSet(viewsets.ModelViewSet):
    queryset = Thirds.objects.all()
    serializer_class = ThirdSerializer
    search_fields = ['name','last_name','second_name','second_last_name', 'nit', 'email', 'phone', 'address', 'city', 'speciality__description','type']
    filterset_fields = ['type','speciality','name','last_name','second_name','second_last_name', 'nit', 'email', 'phone', 'address', 'city', 'speciality__description','type'] # Aqui no hace falta poner citi_id, es obvio que si le pones city le vas a pasar el id

    
class GeneralExamViewSet(viewsets.ModelViewSet):
    queryset = GeneralExam.objects.all()
    serializer_class = GeneralExamSerializer
    search_fields = ['name', 'code']
    
class SystemsReviewViewSet(viewsets.ModelViewSet):
    queryset = SystemsReview.objects.all()
    serializer_class = SystemsReviewSerializer
    search_fields = ['name', 'code']

class ScheduledViewSet(viewsets.ModelViewSet):
    queryset = Scheduled.objects.all()
    serializer_class = ScheduledSerializer
    search_fields = ['date', 'time','third_patient__nit','third_patient__name','third_patient__second_name','third_patient__last_name','third_patient__second_last_name','third_medic__nit','third_medic__name','third_medic__second_name','third_medic__last_name','third_medic__second_last_name','speciality__description']

class ChoicesAPIView(APIView):
    
    def get(self, request):
        choices_data = {
            "TYPE_CHOICES": TYPE_CHOICES,
            "BLOOD_CHOICES": BLOOD_CHOICES,
            "MATERNITY_PREGNANCY_CHOICES": MATERNITY_PREGNANCY_CHOICES,
            "MATERNITY_BREASFEEDING_CHOICES": MATERNITY_BREASFEEDING_CHOICES,
            "MATERNITY_BREASFEEDING_EXTEND_CHOICES": MATERNITY_BREASFEEDING_EXTEND_CHOICES,
            "MATERNITY_BREASFEEDING_COMPLEMENTARY_CHOICES": MATERNITY_BREASFEEDING_COMPLEMENTARY_CHOICES,
            "MATERNITY_VIOLANCE_CHOICES": MATERNITY_VIOLANCE_CHOICES,
            "ETNIAS_CHOICES": ETNIAS_CHOICES,
            "SEX_CHOICES": SEX_CHOICES,
            "TYPE_CHOICES": TYPE_CHOICES,
        }
        return Response(choices_data, status=status.HTTP_200_OK)
    
class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    search_fields = ['third__nit','third__name','third__second_name','third__last_name','third__second_last_name','time','quota','date','start_time','end_time','overflow']
    
    def get_queryset(self):
        queryset = Availability.objects.all()
        third = self.request.query_params.get('third', None)
        if third is not None:
            queryset = queryset.filter(third__id=third)
        return queryset
        