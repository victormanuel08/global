from django.contrib import admin
from django.urls import path, include
from medicalrecords.views import *
from rest_framework import routers
from users.views import GroupViewSet, PermissionListView, UserViewSet

router = routers.DefaultRouter()
router.register('cities', CityViewSet)
router.register('diagnoses', DiagnosisViewSet)
router.register('records', RecordViewSet)
router.register('specialities', SpecialityViewSet)
router.register('thirds', ThirdViewSet)
router.register('auth/groups', GroupViewSet)
router.register('auth/users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/permissions/', PermissionListView.as_view()), # Esto no es una viewset, es una vista solo de leer, no se registra en el router
    path('', include(router.urls))
]

