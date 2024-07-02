from rest_framework import serializers
from medicalrecords.models import *
from medicalrecords.serializers import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'
        

    
class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnoses
        fields = '__all__'

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'
        
class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialities
        fields = '__all__'
        
class ThirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thirds
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
    class Meta:
        model = Scheduled
        fields = '__all__'
        
        
