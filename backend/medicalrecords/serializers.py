from rest_framework import serializers
from medicalrecords.models import *
from medicalrecords.serializers import *
from .models import Thirds
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'
    
class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnoses
        fields = '__all__'

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialities
        fields = '__all__'
        
class ThirdSerializer(serializers.ModelSerializer):    
    speciality_full = SpecialitySerializer(source = 'speciality', read_only=True)
    class Meta:
        model = Thirds
        fields = '__all__'        

class RecordSerializer(serializers.ModelSerializer):    
    third_patient_full = ThirdSerializer(source = 'third_patient', read_only=True)
    third_medic_full = ThirdSerializer(source = 'third_medic', read_only=True)
    diagnosis_full = DiagnosisSerializer(source = 'diagnosis', read_only=True)
    class Meta:
        model = Records
        fields = '__all__'     
        
class GeneralExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralExam
        fields = '__all__'
        
class SystemsReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemsReview
        fields = '__all__'
        
class ScheduledSerializer(serializers.ModelSerializer):
    third_patient_full = ThirdSerializer(source = 'third_patient', read_only=True)
    third_medic_full = ThirdSerializer(source = 'third_medic', read_only=True)
    speciality_full = SpecialitySerializer(source = 'speciality', read_only=True)
    class Meta:
        model = Scheduled
        fields = '__all__'
        
        
