from rest_framework import serializers
from medicalrecords.models import *
from medicalrecords.serializers import *
from .models import Thirds
from datetime import datetime, timedelta
from users.models import User
import pytz
from datetime import datetime


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
        
class ServiceSerializer(serializers.ModelSerializer):
    speciality_full = SpecialitySerializer(source = 'speciality', read_only=True)
    
    class Meta:
        model = Services
        fields = '__all__'
        
class VehicleOnlySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vehicles
        fields = '__all__'
        
class AccidentSerializer(serializers.ModelSerializer):
 
    
    class Meta:
        model = Accidents
        fields = '__all__'
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class ThirdSerializer(serializers.ModelSerializer):    
    speciality_full = SpecialitySerializer(source = 'speciality', read_only=True)    
    city_birth_full = CitySerializer(source = 'city_birth', read_only=True)   
    city_full = CitySerializer(source = 'city', read_only=True) 
    vehicle_full = VehicleOnlySerializer(source = 'vehicle', read_only=True)
    user_full = CustomUserSerializer(source='user', read_only=True) 
    namenit = serializers.SerializerMethodField()

    def get_namenit(self, obj):
        if obj.type_document == 'NI':
            return f"{obj.nit} - {obj.name}"
        else:
            return f"{obj.nit} - {obj.name} {obj.second_name} {obj.last_name} {obj.second_last_name}"

    class Meta:
        model = Thirds
        fields = '__all__'    
        
class VehicleSerializer(serializers.ModelSerializer):
    third_driver_full = ThirdSerializer(source = 'third_driver', read_only=True)
    third_entity_full = ThirdSerializer(source = 'third_entity', read_only=True)
    placamovil = serializers.SerializerMethodField()

    def get_placamovil(self, obj):
        return f"{obj.plate} - {obj.brand}"
        
    class Meta:
        model = Vehicles
        fields = '__all__'
        
class PolicySerializer(serializers.ModelSerializer):
    third_entity_full = ThirdSerializer(source = 'third_entity', read_only=True)


    
    class Meta:
        model = Policy
        fields = '__all__'

    
class FeeSerializer(serializers.ModelSerializer):
    service_full = ServiceSerializer(source = 'service', read_only=True)
    speciality_full = SpecialitySerializer(source = 'speciality', read_only=True)
    third_entity_full = ThirdSerializer(source = 'third_entity', read_only=True)
    
    
    class Meta:
        model = Fees
        fields = '__all__'
         
      

    


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
        
class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedures
        fields = '__all__'
        

class PoliceSerializer(serializers.ModelSerializer):
    third_entity_full = ThirdSerializer(source = 'third_entity', read_only=True)
    vehicle_full = VehicleSerializer(source = 'vehicle', read_only=True)
    fees = FeeSerializer(many=True, read_only=True)     

    class Meta:
        model = Policy
        fields = '__all__'     
    
        

class RecordSerializer(serializers.ModelSerializer):    
    third_patient_full = ThirdSerializer(source = 'third_patient', read_only=True)
    third_medic_full = ThirdSerializer(source = 'third_medic', read_only=True)    
    third_medic_clinic_full = ThirdSerializer(source = 'third_medic_clinic', read_only=True)    
    third_entity_full = ThirdSerializer(source = 'third_entity', read_only=True)
    third_buddy_full = ThirdSerializer(source = 'third_buddy', read_only=True)
    # third_relationship_full = ThirdSerializer(source = 'third_relationship', read_only=True)
    third_clinic_full = ThirdSerializer(source = 'third_clinic', read_only=True)
    third_obj_full =ThirdSerializer(source = 'third_obj', read_only=True)  
    third_driver_full=ThirdSerializer(source = 'third_driver', read_only=True)
    diagnosis_full = DiagnosisSerializer(source = 'diagnosis', read_only=True)
    diagnosis_multi_full = serializers.SerializerMethodField()
    diagnosis_1_full = DiagnosisSerializer(source = 'diagnosis_1', read_only=True)
    diagnosis_2_full = DiagnosisSerializer(source = 'diagnosis_2', read_only=True)
    diagnosis_3_full = DiagnosisSerializer(source = 'diagnosis_3', read_only=True)
    policy_full = PoliceSerializer( source = 'policy' ,  read_only = True)
    vehicle_full = VehicleSerializer(source = 'vehicle', read_only=True)
    # service_full = ServiceSerializer(source = 'service', read_only=True)
    fee_full = FeeSerializer(source = 'fee', read_only=True)
    city_full = CitySerializer(source = 'city', read_only=True)
    records_details = serializers.SerializerMethodField()
    #crear un date time formateado basado en date_time
    date_time_format = serializers.SerializerMethodField()
       
    class Meta:
        model = Records
        fields = '__all__'  
    
    def get_date_time_format(self, obj):        
        bogota_tz = pytz.timezone('America/Bogota')        
        date_time_bogota = obj.date_time.astimezone(bogota_tz)       
        return date_time_bogota.strftime('%Y-%m-%d %I:%M:%S %p') 
  
        
    def get_records_details(self, obj):
        records_details = Records_details.objects.filter(record=obj)
        return RecordDetailSerializer(records_details, many=True).data
        
    def get_diagnosis_multi_full(self, obj):
        diagnosis_multi = obj.diagnosis_multiple.all()
        return DiagnosisSerializer(diagnosis_multi, many=True).data
    
class ScheduledSerializer(serializers.ModelSerializer):
    third_patient_full = ThirdSerializer(source = 'third_patient', read_only=True)
    third_medic_full = ThirdSerializer(source = 'third_medic', read_only=True)
    speciality_full = SpecialitySerializer(source = 'speciality', read_only=True)
    
    fee_full = FeeSerializer(source = 'fee', read_only=True)
    policy_full = PolicySerializer(source = 'policy', read_only=True)
    service_full = ServiceSerializer(source = 'service', read_only=True)
    
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

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Values
        fields = '__all__'
        
class MedicamentsRecordsSerializer(serializers.ModelSerializer):
    service_full =ServiceSerializer(source = 'service', read_only=True)
    
    class Meta:
        model = MedicamentsRecords
        fields = '__all__'
   