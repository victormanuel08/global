from django.conf import settings
from django.http import HttpResponse
from utils.pdf import render_to_pdf
from .models import *
from .serializers import *
from .models import *
from datetime import timedelta
from django.utils import timezone
from rest_framework import viewsets

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views.generic import ListView,View
import requests
from django.core.mail import EmailMessage
from rest_framework.decorators import api_view, action
from django.views.decorators.csrf import csrf_exempt
 
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache 

from django_filters import rest_framework as filters

import cv2
import numpy as np 
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.models import User  # Importa el modelo de usuario predeterminado de Django




class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all().order_by('speciality__description', 'description')
    serializer_class = ServiceSerializer
    search_fields = {
                     
                     'description': ['icontains'],
                        'speciality__description': ['icontains'],
                        'code': ['exact'],
                        'amount_soat': ['gt', 'lt'],
                        'amount_particular': ['gt', 'lt'],
               
    }
    filterset_fields={
        'code': ['exact'],
        'description': ['icontains'],
        'speciality': ['exact'],
        'amount_soat': ['gt', 'lt'],
        'amount_particular': ['gt', 'lt'],                  
    }

    #def get_queryset(self):
    #    queryset = super().get_queryset()
    #    amount_gt = self.request.query_params.get('amount_particular__gt')
    #    amount_soat_gt = self.request.query_params.get('amount_soat__gt')  # Nuevo filtro para monto SOAT
    #    description = self.request.query_params.get('description')
    #    speciality= self.request.query_params.get('speciality')
#
    #    if amount_gt:
    #        queryset = queryset.filter(amount_particular__gt=float(amount_gt))
    #    if amount_soat_gt:
    #        queryset = queryset.filter(amount_soat__gt=float(amount_soat_gt))
    #    if description:         
    #        queryset = queryset.filter(category__name__icontains=description)
    #    if speciality:
    #        queryset = queryset.filter(speciality=speciality)
#
    #    return queryset

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer
    search_fields = ['plate', 'brand','vehicle_type','third_driver__nit','third_driver__name','third_driver__second_name','third_driver__last_name','third_driver__second_last_name']
    filterset_fields=['plate', 'brand','vehicle_type','third_driver__nit','third_driver__name','third_driver__second_name','third_driver__last_name','third_driver__second_last_name']




class AccidentViewSet(viewsets.ModelViewSet):
    queryset = Accidents.objects.order_by('-date_time')  # Los accidentes más recientes
    serializer_class = AccidentSerializer
    search_fields = ['date_time', 'external_cause', 'half', 'vehicle_type']
    filterset_fields = ['date_time', 'external_cause', 'half', 'vehicle_type']

    # Acción personalizada para obtener los accidentes de las últimas 3 horas
    @action(detail=False, methods=['get'])
    def last_3_hours(self, request):
        # Calcular la hora actual menos 3 horas
        three_hours_ago = timezone.now() - timedelta(hours=3)
        
        # Filtrar los accidentes ocurridos en las últimas 3 horas
        accidents_last_3_hours = Accidents.objects.filter(date_time__gte=three_hours_ago)
        
        # Serializar los accidentes y devolver la respuesta
        serializer = self.get_serializer(accidents_last_3_hours, many=True)
        return Response(serializer.data)

    # Acción personalizada para obtener todos los accidentes (sin filtros de tiempo)
    @action(detail=False, methods=['get'])
    def allday(self, request):
        # Obtener todos los accidentes del día actual
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        accidents_today = Accidents.objects.filter(date_time__gte=today_start)
        
        # Serializar los accidentes y devolver la respuesta
        serializer = self.get_serializer(accidents_today, many=True)
        return Response(serializer.data)


    
class ValuesViewSet(viewsets.ModelViewSet):
    queryset = Values.objects.all()
    serializer_class = ValueSerializer
    search_fields = ['type_values', 'amount', 'year_date']
    filterset_fields=['type_values', 'amount', 'year_date']
    
class PoliceViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PoliceSerializer
    search_fields = ['type_police','payment_model','name','description','date_start','date_end','third_entity__name','third_entity__nit']
    filterset_fields=['third_entity__nit','type_police','payment_model','name','description','date_start','date_end']
    
    
 
    
class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fees.objects.all().order_by('specialities__description', 'service__description')
    serializer_class = FeeSerializer
    search_fields = [ 'description','specialities__description','service__description']
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
    queryset = Records.objects.all().order_by('-date_time')  # Los registros más recientes
    serializer_class = RecordSerializer
    
    search_fields = ['date_time','third_patient__nit','third_patient__name','third_patient__second_name','third_patient__last_name','third_patient__second_last_name','third_medic__nit','third_medic__name','third_medic__second_name','third_medic__last_name','third_medic__second_last_name','diagnosis__name','diagnosis__description','number_report']
    filterset_fields = ['date_time','third_patient__nit','third_patient__name','third_patient__second_name','third_patient__last_name','third_patient__second_last_name','third_medic__nit','third_medic__name','third_medic__second_name','third_medic__last_name','third_medic__second_last_name','diagnosis__name','diagnosis__description','number_report']
    
    def perform_create(self, serializer):
        instance = serializer.save()
        diagnosis_ids = self.request.data.get('diagnosis_ids', [])
        print(f"Creating record with diagnosis_ids: {diagnosis_ids}")
        instance.diagnosis_multiple.set(diagnosis_ids)
        instance.save()

    def perform_update(self, serializer):
        instance = serializer.save()    
        diagnosis_ids = self.request.data.get('diagnosis_multi', [])
        print(f"Updating record with diagnosis_ids: {diagnosis_ids}")
        instance.diagnosis_multiple.set(diagnosis_ids)    
        instance.save()
        
    def update(self, request, *args, **kwargs): 
        partial = kwargs.pop('partial', False) 
        instance = self.get_object() 
        serializer = self.get_serializer(instance, data=request.data, partial=partial) 
        serializer.is_valid(raise_exception=True) 
        
        # Obtener los valores actuales de diagnosis_multiple si no están en la solicitud
        if 'diagnosis_multiple' not in request.data:
            current_diagnosis_ids = list(instance.diagnosis_multiple.values_list('id', flat=True))
            request.data['diagnosis_multiple'] = current_diagnosis_ids
            print(f"Adding current diagnosis_multiple to request data: {current_diagnosis_ids}")
        
        self.perform_update(serializer) 
        
        diagnosis_ids = request.data.get('diagnosis_multiple', [])
        print(f"Updating diagnosis_multiple with: {diagnosis_ids}")
        instance.diagnosis_multiple.set(diagnosis_ids)
        instance.save()
        
        print(f"Final diagnosis_multiple: {instance.diagnosis_multiple.all()}")
        return Response(serializer.data)




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
    



class ThirdFilter(filters.FilterSet):
    type = filters.CharFilter(field_name='type', method='filter_type')
    nit = filters.CharFilter(field_name='nit', method='filter_nit')  # Filtro para nit
    user = filters.NumberFilter(field_name='user', method='filter_user')  # Filtro personalizado para user

    class Meta:
        model = Thirds
        fields = ['type', 'name', 'last_name', 'second_name', 'second_last_name', 'nit', 'type_document', 'speciality']

    def filter_type(self, queryset, name, value):
        if value:
            types = value.split(',')  # Separa los valores por coma
            return queryset.filter(**{f'{name}__in': types})
        return queryset

    def filter_nit(self, queryset, name, value):
        if value:
            return queryset.filter(**{f'{name}__icontains': value})  # Filtra por nit parcial
        return queryset

    def filter_user(self, queryset, name, value):
        if value is not None:
            return queryset.filter(**{f'{name}': value})  # Filtro exacto por ID de usuario
        return queryset

class ThirdViewSet(viewsets.ModelViewSet):
    queryset = Thirds.objects.all()
    serializer_class = ThirdSerializer
    filterset_class = ThirdFilter  
    search_fields = ['type', 'name', 'last_name', 'second_name', 'second_last_name', 'nit', 'type_document', 'speciality__description']
    filterset_fields = {
        'type': ['in', 'exact'],  # Usamos '__in' para permitir varios valores
        'name': ['icontains'],
        'last_name': ['icontains'],
        'second_name': ['icontains'],
        'second_last_name': ['icontains'],
        'nit': ['icontains'],  # Cambio a 'icontains' para buscar parcialmente el nit
        'type_document': ['exact'],
        'speciality': ['exact'],
        'user': ['exact'],  # Este es solo un filtro adicional que no será utilizado
    }



    def perform_create(self, serializer):
        instance = serializer.save()
        policy_ids = self.request.data.get('policys', [])
        print(f"Creating third with policy_ids: {policy_ids}")
        instance.policys.set(policy_ids)
        instance.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        policy_ids = self.request.data.get('policys', [])
        print(f"Updating third with policy_ids: {policy_ids}")
        instance.policys.set(policy_ids)
        instance.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # Obtener los valores actuales de policys si no están en la solicitud
        if 'policys' not in request.data:
            current_policy_ids = list(instance.policys.values_list('id', flat=True))
            request.data['policys'] = current_policy_ids
            print(f"Adding current policys to request data: {current_policy_ids}")

        self.perform_update(serializer)

        policy_ids = request.data.get('policys', [])
        print(f"Updating policys with: {policy_ids}")
        instance.policys.set(policy_ids)
        instance.save()

        print(f"Final policys: {instance.policys.all()}")
        return Response(serializer.data)

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
            # Verifica que la estructura sea la esperada antes de acceder a los índices
            if len(choice) >= 4:
                if sex == "M" and choice[2] and choice_id in choice[2].split(','):
                    return {"id": choice[0], "name": choice[1], "details": choice[2]}
                elif sex == "F" and choice[3] and choice_id in choice[3].split(','):
                    return {"id": choice[0], "name": choice[1], "details": choice[3]}
        return None

    def get(self, request, choice_type, choice_id, sex):
        # Verifica que choice_type sea válido
        choices_data = {
            "BODY_PART_CHOICES": BODY_PART_CHOICES,
            "BODY_PART_SIDE_CHOICES": BODY_PART_SIDE_CHOICES,
        }

        if choice_type not in choices_data:
            return Response({"error": "Tipo de elección no válido"}, status=status.HTTP_400_BAD_REQUEST)

        selected_choice = self.get_choice_by_id(choices_data[choice_type], choice_id, sex)

        if selected_choice:
            return Response(selected_choice, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Opción no encontrada"}, status=status.HTTP_404_NOT_FOUND)



    
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

@method_decorator(never_cache, name='dispatch')
class RecordListView(ListView):
    context_object_name = "records"

    TEMPLATE_MAPPING = {
        "ambulancia": (Records, "record_list.html"),
        "thirds": (Thirds, "thirds_list.html"),
        "medicamnetos": (MedicamentsRecords, "medicamentos_list.html"),
    }

    def get_queryset(self):
        template_type = self.kwargs.get("template_type")
        template_id = self.kwargs.get("template_id")
        model, template_name = self.TEMPLATE_MAPPING.get(template_type, (Records, "default_list.html"))
        self.template_name = template_name

        if template_type == "medicamnetos":
            return model.objects.filter(record=template_id)
        return model.objects.filter(id=template_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        template_id = self.kwargs.get("template_id")
        record = Records.objects.filter(id=template_id).first()

        if record:
            def get_image_url(field):
                if field and hasattr(field, 'name') and field.name:
                    return field.url
                return 'records/HCBASIC.jpeg'

            context.update({
                "imgcc": get_image_url(record.imghd),
                "imgso": get_image_url(record.imgso),
                "imgtp": get_image_url(record.imgtp),
                "imgic": get_image_url(record.imgic),
                "imglc": get_image_url(record.imglc),
                "imgls": get_image_url(record.imgls),
            })

            glasgow_ro = int(record.glasgow_ro or 0)
            glasgow_rv = int(record.glasgow_rv or 0)
            glasgow_rm = int(record.glasgow_rm or 0)
            record.glassgow_total = glasgow_ro + glasgow_rv + glasgow_rm

            medicaments = MedicamentsRecords.objects.filter(record=record)
            context['medicaments'] = medicaments

        context["document"] = record
        return context

@method_decorator(never_cache, name='dispatch')
class RecordPdf(RecordListView, View):
    def get(self, request, *args, **kwargs):
        try:
            template_id = kwargs.get('template_id')
            template_type = request.GET.get('template_type', 'ambulancia')
            self.object_list = self.get_queryset()
            context = self.get_context_data(object_list=self.object_list)

            if isinstance(context, HttpResponse):
                return context

            pdf = render_to_pdf(self.template_name, context)
            if not pdf:
                return HttpResponse("Error al generar el PDF", status=500)

            response = HttpResponse(pdf, content_type="application/pdf")
            response["Content-Disposition"] = 'inline; filename="report.pdf"'  # Cambiar a 'attachment' si deseas forzar la descarga
            response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
            response["Pragma"] = "no-cache"
            return response

        except Exception as e:
            return HttpResponse(f"Error al procesar la solicitud: {e}", status=500)


class GeocodeView(APIView):
    def get(self, request, *args, **kwargs):
        coordinates_str = request.query_params.get("coordinates")

        # Validación inicial de las coordenadas
        if not coordinates_str:
            return Response({"error": "Faltan las coordenadas en la solicitud."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            lat, lng = map(float, coordinates_str.split(","))
        except ValueError:
            return Response({"error": "Coordenadas inválidas. Asegúrate de que el formato sea 'lat,lng'."}, status=status.HTTP_400_BAD_REQUEST)

        # URLs de las APIs
        api_key = settings.DISTANCE_MATRIX_API_KEY
        distance_matrix_url = f"https://api-v2.distancematrix.ai/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}"
        nominatim_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lng}&zoom=18&addressdetails=1"
        headers = {'User-Agent': 'GLOBALSAFEIPS/1.0 (ambulancia.globalsafe@gmail.com)'}

        response_data = []

        # Llamada a la API de Distance Matrix
        try:
            distance_matrix_response = requests.get(distance_matrix_url)
            distance_matrix_response.raise_for_status()
            distance_matrix_data = distance_matrix_response.json()

            # Validar que los datos tengan la estructura esperada
            if "result" in distance_matrix_data and len(distance_matrix_data["result"]) > 0:
                result = distance_matrix_data["result"][0]
                response_data.append({
                    "formatted_address": result.get("formatted_address", "No disponible"),
                    "address_components": result.get("address_components", []),
                })
                print(f"DistanceMatrix: {result.get('formatted_address')}")
            else:
                print("DistanceMatrix: Respuesta vacía o sin resultados.")
        except requests.RequestException as e:
            print(f"Error al llamar a DistanceMatrix API: {e}")
        except KeyError:
            print("Error procesando los datos de DistanceMatrix: Estructura inesperada en el JSON.")

        # Llamada a la API de Nominatim
        try:
            nominatim_response = requests.get(nominatim_url, headers=headers)
            nominatim_response.raise_for_status()
            nominatim_data = nominatim_response.json()

            # Validar la estructura del JSON
            if "display_name" in nominatim_data and "address" in nominatim_data:
                address = nominatim_data["address"]
                response_data.append({
                    "formatted_address": nominatim_data["display_name"],
                    "address_components": {
                        "road": address.get("road", "No disponible"),
                        "neighbourhood": address.get("neighbourhood", "No disponible"),
                        "city_district": address.get("city_district", "No disponible"),
                        "city": address.get("city", "No disponible"),
                        "county": address.get("county", "No disponible"),
                        "postcode": address.get("postcode", "No disponible"),
                        "country": address.get("country", "No disponible"),
                    },
                })
                print(f"Nominatim: {nominatim_data['display_name']}")
            else:
                print("Nominatim: Respuesta vacía o sin resultados.")
        except requests.RequestException as e:
            print(f"Error al llamar a Nominatim API: {e}")
        except KeyError:
            print("Error procesando los datos de Nominatim: Estructura inesperada en el JSON.")

        # Responder con los datos recolectados
        if not response_data:
            return Response({"error": "No se pudo obtener información de las APIs."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response_data, status=status.HTTP_200_OK)

    
@api_view(['POST'])
@csrf_exempt
def sendemail(request):
    template_id = request.data.get('id', None)
    template_type = request.data.get('type', 'ambulancia')  # Por defecto, "ambulancia"
    emails = Values.objects.filter(type_values='ED').values_list('val', flat=True)
    
    if not template_id:
        return Response({'error': 'ID del template no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)
    
    if template_type == 'ambulancia':
        record = Records.objects.filter(id=template_id).first()
        if not record:
            return Response({'error': 'No se encontró el registro de ambulancia'}, status=status.HTTP_404_NOT_FOUND)
        
        paciente = Thirds.objects.filter(nit=record.third_patient).first()
        auxiliar = Thirds.objects.filter(nit=record.third_medic).first()
        medico = Thirds.objects.filter(nit=record.third_medic_clinic).first()
        conductor = Thirds.objects.filter(nit=record.third_driver).first()
        
        mensaje = f"""
        **Paciente:** {paciente.name} {paciente.last_name}
        **Médico:** {medico.name} {medico.last_name}
        **Auxiliar:** {auxiliar.name} {auxiliar.last_name}
        **Conductor:** {conductor.name} {conductor.last_name}
        """
        filename = f"GATA-HC-{paciente.nit}"
        template_name = "record_list.html"
        data = {'document': record}
    
    elif template_type == 'medicamentos':
        record = Records.objects.filter(id=template_id).first()
        medicamentos = MedicamentsRecords.objects.filter(record=template_id)
        if not medicamentos.exists():
            return Response({'error': 'No se encontraron medicamentos asociados'}, status=status.HTTP_404_NOT_FOUND)
        
        mensaje = f"Se encontraron {medicamentos.count()} medicamentos asociados al registro."
        for med in medicamentos:
            mensaje += f"\n- {med.service.description} ({med.quantity}) - {med.dose} vía {med.route}"
        
        filename = f"GATA-MEDS-{template_id}"
        template_name = "medicamentos_list.html"
        data = {'document': record, 'medicamentos': medicamentos}
    
    else:
        return Response({'error': 'Tipo de template no reconocido'}, status=status.HTTP_400_BAD_REQUEST)
    
    pdf = render_to_pdf(template_name, data)  # render_to_pdf debe devolver un objeto tipo `bytes`
    
    if pdf is None:
        return Response({'error': 'No se pudo generar el PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    try:
        email = EmailMessage(
            subject=f'Reporte {template_type.capitalize()} {filename}',
            body=mensaje,
            from_email='noreply@globalsafeips.com.co',
            to=list(emails),
        )
        email.attach(f"{filename}.pdf", pdf, 'application/pdf')  # Corrige el error
        email.send()
        return Response({'mensaje': 'Correo enviado correctamente'})
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ImageProcessingView(APIView):
    def post(self, request, *args, **kwargs):
        record_id = request.data.get("record_id")
        if record_id:
            record = get_object_or_404(Records, id=record_id)
            image_path = record.imghd.path
            image = Image.open(image_path)
            image = np.array(image)
            blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
            edges = cv2.Canny(binary, 100, 200)
            result_image = Image.fromarray(edges)
            inverted_image = 255 - np.array(result_image)
            
            try:
                buffer = BytesIO()
                Image.fromarray(inverted_image).save(buffer, format="JPEG")  # Cambio a formato PNG
                result_image_bytes = buffer.getvalue()

                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                filename = f"HDProcessed_{timestamp}.jpeg"

                record.imghdr.save(filename, ContentFile(result_image_bytes))
                record.save()

                print(f"Imagen guardada como {filename}")
                return Response({'message': f'Imagen procesada y guardada como {filename}'}, status=status.HTTP_200_OK)
            except Exception as e:
                print(f"Error al guardar la imagen: {str(e)}")
                return Response({'error': 'Error al guardar la imagen'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'Se requiere un record_id válido'}, status=status.HTTP_400_BAD_REQUEST)
        


def kc(request):
    response = HttpResponse("Cookie borrada")
    response.delete_cookie('token')
    return response

class SetPasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user.set_password(request.data['new_password'])
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MedicamentsRecordsViewSet(viewsets.ModelViewSet):
    queryset = MedicamentsRecords.objects.all()
    serializer_class = MedicamentsRecordsSerializer
    search_fields = ['record','services__description','services__code']
    filterset_fields = ['record']
    

    
