from .models import *
from .serializers import *
from .models import Cities, Diagnoses, Records, Specialities, Thirds, GeneralExam, SystemsReview, Scheduled, Availability
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Q

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    search_fields = [ 'code', 'description','speciality','amount_soat','amount_particular']
    filterset_fields=['code', 'description','speciality','amount_soat','amount_particular']

    def get_queryset(self):
        queryset = super().get_queryset()
        amount_gt = self.request.query_params.get('amount_particular__gt')
        amount_soat_gt = self.request.query_params.get('amount_soat__gt')  # Nuevo filtro para monto SOAT
        if amount_gt:
            queryset = queryset.filter(amount_particular__gt=float(amount_gt))
        if amount_soat_gt:
            queryset = queryset.filter(amount_soat__gt=float(amount_soat_gt))
        return queryset

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer
    search_fields = ['plate', 'brand']
    
class PoliceViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PoliceSerializer
    search_fields = ['plate', 'brand']
    
 
    
class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fees.objects.all()
    serializer_class = FeeSerializer
    search_fields = ['code', 'description','specialities','third_entity','service','policy']
    filterset_fields=['code', 'description','specialities','third_entity','service','policy']
    
    @receiver(pre_save, sender=Fees)
    def update_description(sender, instance, **kwargs):
        # Consultar la entidad Policy
        try:
            policy_entity = Policy.objects.get(id=instance.policy_id)
            # Combinar nombre y descripción
            combined_description = f"{policy_entity.name} - {policy_entity.description}"
            # Asignar al campo description en Fees
            instance.description = combined_description
        except Policy.DoesNotExist:
            # Manejar el caso en que no se encuentre la entidad Policy
            pass




    
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
    search_fields = ['third_patient', 'third_patient__nit','policy'] 
    filterset_fields = ['third_patient', 'third_patient__nit','policy']# Otras búsquedas   


class RecordDetailViewSet(viewsets.ModelViewSet):
    queryset = Records_details.objects.all()
    serializer_class = RecordDetailSerializer
    search_fields = ['record']    
    
class RecordDetailsOnlyViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            record = Records.objects.get(pk=pk)
            serialized_data = RecordDetailsOnlySerializer(record).data
            return Response(serialized_data)
        except Records.DoesNotExist:
            return Response({"error": "Registro no encontrado"}, status=404)
    

class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Specialities.objects.all()
    serializer_class = SpecialitySerializer
    search_fields = ['code','description','id']
    filterset_fields = ['code','description','id']
    
class ProceduresViewSet(viewsets.ModelViewSet):
    queryset = Procedures.objects.all()
    serializer_class = ProcedureSerializer
    search_fields = ['code','description']

class ThirdViewSet(viewsets.ModelViewSet):
    queryset = Thirds.objects.all()
    serializer_class = ThirdSerializer
    # search_fields = ['name','last_name','second_name','second_last_name', 'nit', 'email', 'phone', 'address', 'city', 'speciality__description','type']
    #filterset_fields = ['type','type_document','speciality','name','last_name','second_name','second_last_name', 'nit', 'email', 'phone', 'address', 'city', 'speciality__description','type']
    search_fields = ['type','name','last_name','second_name','second_last_name', 'nit', 'type_document']
    filterset_fields = ['type','name','last_name','second_name','second_last_name', 'nit','type_document']
    
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
    search_fields = ['fee_ful__police_full__type_police','speciality','date', 'time','third_patient__nit','third_patient__name','third_patient__second_name','third_patient__last_name','third_patient__second_last_name','third_medic__nit','third_medic__name','third_medic__second_name','third_medic__last_name','third_medic__second_last_name','speciality_full__description']

    def get_queryset(self):
            queryset = super().get_queryset()
            speciality_id = self.request.query_params.get('speciality')
            third_medic_id = self.request.query_params.get('third_medic')
            third_patient_id = self.request.query_params.get('third_patient')
            date = self.request.query_params.get('date')
            date_origin = self.request.query_params.get('date_origin')
            insurance = self.request.query_params.get('insurance')
            fee_full__police_full__type_police = self.request.query_params.get('fee_full__police_full__type_police')
            if fee_full__police_full__type_police:   
                print(f"fee_full__police_full__type_police: {fee_full__police_full__type_police}")            
                queryset = queryset.filter(fee_full__police_full__type_police=fee_full__police_full__type_police)
            if speciality_id:
                queryset = queryset.filter(speciality=speciality_id)
            if third_medic_id:
                queryset = queryset.filter(third_medic=third_medic_id)    
            if third_patient_id:
                queryset = queryset.filter(third_patient=third_patient_id)            
            if date:
                queryset =  queryset.filter(date=date)  
            if insurance:
                queryset =  queryset.filter(insurance=insurance)  
            if date_origin:
                queryset =  queryset.filter(date_origin=date_origin)
            return queryset

class ChoicesAPIView(APIView):    
    def get_choice_by_id(self, choice_list, choice_id):
        for choice in choice_list:
            if choice[0] == choice_id:
                return {"id": choice[0], "name": choice[1]}
        return None
    
    def get(self, request):
        choices_data = {
            "TYPE_CHOICES": TYPE_CHOICES,
            "BLOOD_CHOICES": BLOOD_CHOICES,
            "MATERNITY_PREGNANCY_CHOICES": MATERNITY_PREGNANCY_CHOICES,
            "MATERNITY_CHOICES": MATERNITY_BREASFEEDING_CHOICES,
            "MATERNITY_EXTEND_CHOICES": MATERNITY_BREASFEEDING_EXTEND_CHOICES,
            "MATERNITY_COMPLEMENTARY_CHOICES": MATERNITY_BREASFEEDING_COMPLEMENTARY_CHOICES,
            "MATERNITY_VIOLANCE_CHOICES": MATERNITY_VIOLANCE_CHOICES,
            "ETNIAS_CHOICES": ETNIAS_CHOICES,
            "SEX_CHOICES": SEX_CHOICES,                 
            "STATUS_CHOICES": STATUS_CHOICES,
            "OCCUPATION_CHOICES": OCCUPATION_CHOICES,
            "ZONE_CHOICES": ZONE_CHOICES,
            "TYPE_DOCUMENT_CHOICES": TYPE_DOCUMENT_CHOICES,                       
            "PRIORITY_CHOICES": PRIORITY_CHOICES,
            "RELATIONSHIP_CHOICES": RELATIONSHIP_CHOICES,
            "EXTERNAL_CAUSE_CHOICES": EXTERNAL_CAUSE_CHOICES,
            "VEHICLE_TYPE_CHOICES": VEHICLE_TYPE_CHOICES,
            "GLASGOW_RO_CHOICES": GLASGOW_RO_CHOICES,
            "GLASGOW_RV_CHOICES": GLASGOW_RV_CHOICES,
            "GLASGOW_RM_CHOICES": GLASGOW_RM_CHOICES,
            "HALF_CHOICES": HALF_CHOICES,   
            "BODY_PART_CHOICES": BODY_PART_CHOICES,
            "BODY_PART_SIDE_CHOICES": BODY_PART_SIDE_CHOICES,   
            "PAYMENT_MODEL_CHOICES": PAYMENT_MODEL_CHOICES,
            "TYPE_POLICE_CHOICES": TYPE_POLICE_CHOICES,
        }
        selected_choice_id = "P"
        selected_choice = self.get_choice_by_id(choices_data.get("TYPE_CHOICES", []), selected_choice_id)

        if selected_choice:
            print(f"Objeto seleccionado: {selected_choice}")
        else:
            print(f"No se encontró un objeto con ID {selected_choice_id}")

        return Response(choices_data, status=status.HTTP_200_OK)
    
    
class SearchChoiceAPIView(APIView):
    def get_choice_by_id(self, choice_list, choice_id):
        for choice in choice_list:
            if choice[0] == choice_id:
                result = {"id": choice[0], "name": choice[1]}
                if len(choice) >= 3:
                    result["male"] = choice[2]
                if len(choice) >= 4:
                    result["female"] = choice[3]
                return result
        return None
    


    def get(self, request, choice_type, choice_id):
        choices_data = {
            "TYPE_CHOICES": TYPE_CHOICES,
            "BLOOD_CHOICES": BLOOD_CHOICES,
            "MATERNITY_PREGNANCY_CHOICES": MATERNITY_PREGNANCY_CHOICES,
            "MATERNITY_CHOICES": MATERNITY_BREASFEEDING_CHOICES,
            "MATERNITY_EXTEND_CHOICES": MATERNITY_BREASFEEDING_EXTEND_CHOICES,
            "MATERNITY_COMPLEMENTARY_CHOICES": MATERNITY_BREASFEEDING_COMPLEMENTARY_CHOICES,
            "MATERNITY_VIOLANCE_CHOICES": MATERNITY_VIOLANCE_CHOICES,
            "ETNIAS_CHOICES": ETNIAS_CHOICES,
            "SEX_CHOICES": SEX_CHOICES,                 
            "STATUS_CHOICES": STATUS_CHOICES,
            "OCCUPATION_CHOICES": OCCUPATION_CHOICES,
            "ZONE_CHOICES": ZONE_CHOICES,
            "TYPE_DOCUMENT_CHOICES": TYPE_DOCUMENT_CHOICES,                       
            "PRIORITY_CHOICES": PRIORITY_CHOICES,
            "RELATIONSHIP_CHOICES": RELATIONSHIP_CHOICES,
            "EXTERNAL_CAUSE_CHOICES": EXTERNAL_CAUSE_CHOICES,
            "VEHICLE_TYPE_CHOICES": VEHICLE_TYPE_CHOICES,
            "GLASGOW_RO_CHOICES": GLASGOW_RO_CHOICES,
            "GLASGOW_RV_CHOICES": GLASGOW_RV_CHOICES,
            "GLASGOW_RM_CHOICES": GLASGOW_RM_CHOICES,
            "HALF_CHOICES": HALF_CHOICES,    
            "BODY_PART_CHOICES": BODY_PART_CHOICES,
            "BODY_PART_SIDE_CHOICES": BODY_PART_SIDE_CHOICES,    
            "PAYMENT_MODEL_CHOICES": PAYMENT_MODEL_CHOICES,
            "TYPE_POLICE_CHOICES": TYPE_POLICE_CHOICES,  
        }

        selected_choice = self.get_choice_by_id(choices_data.get(choice_type, []), choice_id)

        if selected_choice:
            return Response(selected_choice, status=status.HTTP_200_OK)
        else:
            return Response( {}, status=status.HTTP_200_OK)
           #return Response({}, status=status.HTTP_404_NOT_FOUND)  
           
class SearchBodyAPIView(APIView):
    def get_choice_by_id(self, choice_list, choice_id, sex):
        for choice in choice_list:
            if sex == "M" and len(choice) >= 2 and choice[2] and choice_id in choice[2]:
                return {"id": choice[0], "name": choice[1], "details": choice[2]}
            elif sex == "F" and len(choice) >= 2 and choice[3] and choice_id in choice[3]:
                return {"id": choice[0], "name": choice[1], "details": choice[3]}
        return None

    def get(self, request, choice_type, choice_id, sex):
        choices_data = {
            "BODY_PART_CHOICES": BODY_PART_CHOICES,
            "BODY_PART_SIDE_CHOICES": BODY_PART_SIDE_CHOICES,
        }

        selected_choice = self.get_choice_by_id(choices_data.get(choice_type, []), choice_id, sex)

        if selected_choice:
            return Response(selected_choice, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_200_OK)



    
class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    search_fields = ['date','third__nit','third__name','third__second_name','third__last_name','third__second_last_name','time','quota','start_time','end_time','overflow']
    
    def get_queryset(self):
        queryset = Availability.objects.all()
        third = self.request.query_params.get('third', None)
        date = self.request.query_params.get('date', None)

        if third is not None:
            queryset = queryset.filter(third__id=third)

        if date is not None:
            queryset = queryset.filter(date=date)

        return queryset
