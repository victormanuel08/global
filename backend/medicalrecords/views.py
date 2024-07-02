from .models import *
from .serializers import *
from .models import Cities, Diagnoses, Records, Specialities, Thirds, GeneralExam, SystemsReview, Scheduled
from rest_framework import viewsets

    
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
    search_fields = ['reason_consutation']

class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Specialities.objects.all()
    serializer_class = SpecialitySerializer
    search_fields = ['code','description']

class ThirdViewSet(viewsets.ModelViewSet):
    queryset = Thirds.objects.all()
    serializer_class = ThirdSerializer
    search_fields = ['name','last_name','second_name','second_last_name' 'nit', 'email', 'phone', 'address', 'city', 'speciality_id']
    
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
    search_fields = ['date', 'time', 'reason', 'record_id', 'third_id', 'speciality_id', 'city_id']

    

