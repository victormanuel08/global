from django.conf import settings
from django.http import HttpResponse
from utils.pdf import render_to_pdf
from .models import *
from .serializers import *
from .models import *
from rest_framework import viewsets

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.views.generic import ListView,View
import requests
from django.core.mail import EmailMessage
from rest_framework.decorators import api_view, action
from django.views.decorators.csrf import csrf_exempt

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
    queryset = Records.objects.all()
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
    
class RecordListView(ListView):
    context_object_name = "records"

    # Definir un mapping para modelos y plantillas
    TEMPLATE_MAPPING = {
        "ambulancia": (Records, "record_list.html"),
        "thirds": (Thirds, "thirds_list.html"),
        "medicamnetos": (MedicamentsRecords, "medicamentos_list.html"),
    }

    def get_queryset(self):
        template_type = self.kwargs.get("template_type")
        template_id = self.kwargs.get("template_id")

        # Validar el tipo de plantilla y obtener modelo/plantilla
        model, template_name = self.TEMPLATE_MAPPING.get(
            template_type, (Records, "default_list.html")
        )
        self.template_name = template_name

        # Realizar la consulta con el modelo correspondiente
        if template_type == "medicamnetos":
            return model.objects.filter(record=template_id)  # Relación con `record`
        return model.objects.filter(id=template_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        template_id = self.kwargs.get("template_id")
        record = Records.objects.filter(id=template_id).first()
        
        if record:
            try:
                # Función para verificar si el campo de imagen tiene archivo adjunto
                def get_image_url(field):
                    if field and hasattr(field, 'name') and field.name:
                        return field.url
                    return 'records/HCBASIC.jpeg'  # Imagen por defecto

                # Actualización de imágenes
                context.update({
                    "imgcc": get_image_url(record.imghd),
                    "imgso": get_image_url(record.imgso),
                    "imgtp": get_image_url(record.imgtp),
                    "imgic": get_image_url(record.imgic),
                    "imglc": get_image_url(record.imglc),
                    "imgls": get_image_url(record.imgls),  # Verificar imgls correctamente
                })

                # Verificar y registrar los valores de glasgow
                glasgow_ro = int(record.glasgow_ro or 0)
                glasgow_rv = int(record.glasgow_rv or 0)
                glasgow_rm = int(record.glasgow_rm or 0)
                record.glassgow_total = glasgow_ro + glasgow_rv + glasgow_rm

                # Agregar los medicamentos al contexto
                medicaments = MedicamentsRecords.objects.filter(record=record)
                context['medicaments'] = medicaments

            except (TypeError, ValueError) as e:
                return HttpResponse("No está totalmente diligenciado", status=400)
        
        context["document"] = record
        return context


class RecordPdf(RecordListView, View):
    def get(self, request, *args, **kwargs):
        try:
            # Obtener el ID de la plantilla y el tipo de plantilla
            template_id = kwargs.get('template_id')
            template_type = request.GET.get('template_type', 'ambulancia')  # Usar 'ambulancia' como valor predeterminado si no se proporciona

            # Obtener el contexto con el queryset
            self.object_list = self.get_queryset()
            context = self.get_context_data(object_list=self.object_list)

            # Validar si el contexto devuelve un error
            if isinstance(context, HttpResponse):
                return context

            # Lógica para manejar diferentes tipos de plantillas
            if template_type == 'medicamentos':
                # Obtener la lista de medicamentos asociados al registro
                medicaments = MedicamentsRecords.objects.filter(record=template_id)
                context['medicaments'] = medicaments

            elif template_type == 'ambulancia':
                # Obtener el registro de ambulancia
                record = Records.objects.filter(id=template_id).first()
                if not record:
                    # Si no se encuentra el registro, generar un error
                    return HttpResponse("Registro no encontrado", status=404)
                context['document'] = record

            # Generar el PDF
            pdf = render_to_pdf(self.template_name, context)
            if not pdf:
                return HttpResponse("Error al generar el PDF", status=500)

            # Preparar la respuesta con el PDF generado
            response = HttpResponse(pdf, content_type="application/pdf")
            response["Content-Disposition"] = f'attachment; filename="report-{template_type}.pdf"'
            return response

        except Exception as e:
            # Manejar cualquier otra excepción
            return HttpResponse(f"Error al procesar la solicitud: {e}", status=500)


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
        medico = Thirds.objects.filter(nit=record.third_medic).first()
        auxiliar = Thirds.objects.filter(nit=record.third_medic_clinic).first()
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
    
    pdf = render_to_pdf(template_name, data)
    
    try:
        email = EmailMessage(
            subject=f'Reporte {template_type.capitalize()} {filename}',
            body=mensaje,
            from_email='noreply@globalsafeips.com.co',
            to=list(emails),
        )
        email.attach(f"{filename}.pdf", pdf.content, 'application/pdf')
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
    

    
