from django.contrib import admin
from django.urls import path, include
from medicalrecords.views import *
from rest_framework import routers
from users.views import GroupViewSet, PermissionListView, UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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
router.register('systems_review', SystemsReviewViewSet)
router.register('availabilities', AvailabilityViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/permissions/', PermissionListView.as_view()), # Esto no es una viewset, es una vista solo de leer, no se registra en el router
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/choices/', ChoicesAPIView.as_view(), name='choices-api'),
    path('records/<int:pk>/records_details/', RecordDetailsOnlyViewSet.as_view({'get': 'retrieve'}), name='record-details'),
    path('', include(router.urls)),
]

