

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from utils.pdf import render_to_pdf
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


from .models import *
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Q
from django.views.generic import ListView,View
from django.shortcuts import render
import requests


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    search_fields = [ 'code', 'description','speciality','amount_soat','amount_particular']
    filterset_fields=['code', 'description','speciality','amount_soat','amount_particular']

    def get_queryset(self):
        queryset = super().get_queryset()
        amount_gt = self.request.query_params.get('amount_particular__gt')
        amount_soat_gt = self.request.query_params.get('amount_soat__gt')  # Nuevo filtro para monto SOAT
        description = self.request.query_params.get('description')

        if amount_gt:
            queryset = queryset.filter(amount_particular__gt=float(amount_gt))
        if amount_soat_gt:
            queryset = queryset.filter(amount_soat__gt=float(amount_soat_gt))
        if description:         
            queryset = queryset.filter(category__name__icontains=description)

        return queryset

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer
    search_fields = ['plate', 'brand','vehicle_type','third_driver__nit','third_driver__name','third_driver__second_name','third_driver__last_name','third_driver__second_last_name']
    filterset_fields=['plate', 'brand','vehicle_type','third_driver__nit','third_driver__name','third_driver__second_name','third_driver__last_name','third_driver__second_last_name']
       
class ValuesViewSet(viewsets.ModelViewSet):
    queryset = Values.objects.all()
    serializer_class = ValueSerializer
    search_fields = ['type_values', 'amount', 'year_date']
    filterset_fields=['type_values', 'amount', 'year_date']
    
class PoliceViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PoliceSerializer
    search_fields = ['plate', 'brand']
    
 
    
class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fees.objects.all()
    serializer_class = FeeSerializer
    search_fields = [ 'description','specialities','third_entity','service','policy']
    filterset_fields=[ 'description','specialities','third_entity','service','policy']
    
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
    search_fields = ['date_time','third_patient__nit','third_patient__name','third_patient__second_name','third_patient__last_name','third_patient__second_last_name','third_medic__nit','third_medic__name','third_medic__second_name','third_medic__last_name','third_medic__second_last_name','diagnosis__name','diagnosis__description','number_report']
    search_fields = ['date_time','third_patient__nit','third_patient__name','third_patient__second_name','third_patient__last_name','third_patient__second_last_name','third_medic__nit','third_medic__name','third_medic__second_name','third_medic__last_name','third_medic__second_last_name','diagnosis__name','diagnosis__description','number_report']


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
            "TYPE_ACCIDENT_CHOICES": TYPE_ACCIDENT_CHOICES,
           
            "VALUES_CHOICES": VALUES_CHOICES,
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
            "TYPE_ACCIDENT_CHOICES": TYPE_ACCIDENT_CHOICES,
         
            "VALUES_CHOICES": VALUES_CHOICES,
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

class RecordListView(ListView):
    context_object_name = "records"

    def get_queryset(self):
        template_type = self.kwargs.get('template_type')
        template_id = self.kwargs.get('template_id')

        # Condicional para determinar qué entidad consultar
        if template_type == 'ambulancia':
            model = Records
            template_name = "record_list.html"
            return Records.objects.filter(id=template_id)
        elif template_type == 'thirds':
            model = Thirds
            template_name = "thirds_list.html"
            return Thirds.objects.filter(id=template_id)
        elif template_type == 'police':
            model = Policy
            template_name = "police_list.html"
            return Thirds.objects.filter(id=template_id)
        else:
            # Si no se encuentra el tipo de plantilla, puedes devolver todos los registros
            return Records.objects.all()  # O Thirds.objects.all() según corresponda

   
   
class RecordPdf(View):
    def get(self, request, *args, **kwargs):
        template_type = self.kwargs.get('template_type')
        template_id = self.kwargs.get('template_id')
       
        if template_type == 'ambulancia':
            records = Records.objects.filter(id=template_id)
            template_name = "record_list.html"
        elif template_type == 'thirds':
            records = Thirds.objects.filter(id=template_id)
            template_name = "thirds_list.html"
        elif template_type == 'police':
            records = Policy.objects.filter(id=template_id)
            template_name = "police_list.html"
        else:
           
            records = Records.objects.all() 

        data = {'records': records}
        pdf = render_to_pdf('record_list.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
  
  


class GeocodeView(APIView):
    def get(self, request, *args, **kwargs):
        coordinates_str = request.query_params.get("coordinates")
        try:
            lat, lng = map(float, coordinates_str.split(","))
        except ValueError:
            return Response({"error": "Coordenadas inválidas"}, status=400)

        api_key = settings.DISTANCE_MATRIX_API_KEY
        distance_matrix_url = f"https://api-v2.distancematrix.ai/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}"
        nominatim_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lng}&zoom=18&addressdetails=1"

        response_data = []

        try:
            distance_matrix_response = requests.get(distance_matrix_url)
            distance_matrix_data = distance_matrix_response.json()
            response_data.append({
                "formatted_address": distance_matrix_data["result"][0]["formatted_address"],
                "address_components": distance_matrix_data["result"][0]["address_components"],
            })
        except requests.RequestException as e:
           
            pass

        try:
            nominatim_response = requests.get(nominatim_url)
            nominatim_data = nominatim_response.json()
            response_data.append({
                "formatted_address": nominatim_data["display_name"],
                "address_components": {
                    "road": nominatim_data["address"]["road"],
                    "neighbourhood": nominatim_data["address"]["neighbourhood"],
                    "city_district": nominatim_data["address"]["city_district"],
                    "city": nominatim_data["address"]["city"],
                    "county": nominatim_data["address"]["county"],
                    "state": nominatim_data["address"]["state"],
                    "postcode": nominatim_data["address"]["postcode"],
                    "country": nominatim_data["address"]["country"],
                },
            })
        except requests.RequestException as e:
           
            pass

        return Response(response_data)
