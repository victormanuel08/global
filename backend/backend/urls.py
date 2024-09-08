
from django.urls import path, include
from django.contrib import admin

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, 
)

from django.conf import settings
from django.conf.urls.static import static
from medicalrecords import views
from medicalrecords.views import *
from medicalrecords.views import sendemail

from users.views import GroupViewSet, PermissionListView, UserViewSet



router = routers.DefaultRouter()
router.register('cities', CityViewSet)
router.register('diagnoses', DiagnosisViewSet)
router.register('records', RecordViewSet)
router.register('records_details', RecordDetailViewSet)
router.register('specialities', SpecialityViewSet)
router.register('thirds', ThirdViewSet)
router.register('scheduleds', ScheduledViewSet)

router.register('auth/groups', GroupViewSet)
router.register('auth/users', UserViewSet)

router.register('general_exam', GeneralExamViewSet)
router.register('procedures', ProceduresViewSet)
router.register('systems_review', SystemsReviewViewSet)
router.register('availabilities', AvailabilityViewSet)
router.register('vehicles', VehicleViewSet)
router.register('polices', PoliceViewSet)
router.register('fees', FeeViewSet)
router.register('services', ServiceViewSet)
router.register('values', ValuesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/permissions/', PermissionListView.as_view()), # Esto no es una viewset, es una vista solo de leer, no se registra en el router
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/choices/', ChoicesAPIView.as_view(), name='choices-api'),
    path('geocode/', GeocodeView.as_view(), name='geocode'),
    path('sendemail/',sendemail, name='sendemail'),
    path('processimage/',ImageProcessingView.as_view(), name='processimage'),

    path('api/pdf/<str:template_type>/<str:template_id>/', views.RecordListView.as_view(), name='template-pdf'),
    path('api/printpdf/<str:template_type>/<int:template_id>/', views.RecordPdf.as_view(), name='print-pdf'),
    # path('api/choices/', ChoicesAPIView.as_view(), name='choices-api'),
    path('api/choices/', ChoicesAPIView.as_view(), name='choices-list'),
    path('api/choices/<str:choice_type>/<str:choice_id>/', SearchChoiceAPIView.as_view(), name='search-choice'),
    path('api/choices/<str:choice_type>/<str:choice_id>/<str:sex>/', SearchBodyAPIView.as_view(), name='search-choice'), 
    path('records/<int:pk>/records_details/', RecordDetailsOnlyViewSet.as_view({'get': 'retrieve'}), name='record-details'),
    
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
