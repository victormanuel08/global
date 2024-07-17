from rest_framework import serializers
from medicalrecords.models import *
from medicalrecords.serializers import *
from .models import Thirds
from datetime import datetime, timedelta

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
    diagnosis_1_full = DiagnosisSerializer(source = 'diagnosis_1', read_only=True)
    diagnosis_2_full = DiagnosisSerializer(source = 'diagnosis_2', read_only=True)
    diagnosis_3_full = DiagnosisSerializer(source = 'diagnosis_3', read_only=True)
    records_details = serializers.SerializerMethodField()
    class Meta:
        model = Records
        fields = '__all__'  
    
    def get_records_details(self, obj):
        records_details = Records_details.objects.filter(record=obj)
        return RecordDetailSerializer(records_details, many=True).data

class RecordDetailsOnlySerializer(serializers.ModelSerializer):
    records_details = serializers.SerializerMethodField()
    class Meta:
        model = Records
        fields = ('records_details',)
    
    def get_records_details(self, obj):
        records_details = Records_details.objects.filter(record=obj)
        return RecordDetailSerializer(records_details, many=True).data

    def to_representation(self, instance):
        # Obtén los detalles de los registros
        records_details = Records_details.objects.filter(record=instance)

        # Transforma los detalles de los registros según tu nuevo formato
        transformed_data = {
            "count": records_details.count(),
            "next": None,
            "previous": None,
            "results": RecordDetailSerializer(records_details, many=True).data
        }

        return transformed_data

        
class RecordDetailSerializer(serializers.ModelSerializer):
    #record_full = RecordSerializer(source = 'record', read_only=True)
    class Meta:
        model = Records_details
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
        
class AvailabilitySerializer(serializers.ModelSerializer):
    third_medic_full = ThirdSerializer(source = 'third', read_only=True)
    day = serializers.SerializerMethodField() # aca deberia salir el dia Lunes Martes etc correspondiente a esa fecha a date 
    rangetime = serializers.SerializerMethodField() # aca deberia salir el rango de tiempo correspondiente a esa fecha a date
    class Meta:
        model = Availability
        fields = '__all__'
        
    def get_day(self, obj):
        # Mapeo de nombres de días en español
        dias = {
            'Monday': 'Lunes',
            'Tuesday': 'Martes',
            'Wednesday': 'Miércoles',
            'Thursday': 'Jueves',
            'Friday': 'Viernes',
            'Saturday': 'Sábado',
            'Sunday': 'Domingo',
        }
        
        day_of_week = obj.date.strftime('%A')
        return dias.get(day_of_week, day_of_week)  

    def get_rangetime(self, obj):# debe buscar otras filas en esta entidad que tengan el mismo third(asi se llama el campo) y el mismo dia(date se llama el campo ) y devolver los rangos de tiempo unidos pero no repetidos de todas la sposibilidades        
        num_intervals = obj.quota  
        intervals = []
        current_time = datetime.combine(datetime.today(), obj.start_time)
        for i in range(1, num_intervals + 1):
            time_start = current_time.strftime('%H:%M:%S')
            current_time += timedelta(minutes=int(obj.time), seconds=int((obj.time - int(obj.time)) * 60))
            time_end = current_time.strftime('%H:%M:%S')
            inter = f"{time_start} - {time_end}"
            if obj.overflow > 0:
                inter = f"{time_start} - {time_end} ({obj.overflow})"
            
            overflow = obj.overflow
            intervals.append({"id": i, "time_start": time_start, "time_end": time_end, "overflow": overflow, "inter": inter})

        return intervals
