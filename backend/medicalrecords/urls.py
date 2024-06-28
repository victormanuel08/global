from medicalrecords.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'diagnoses', DiagnosisViewSet)
router.register(r'records', RecordViewSet)
router.register(r'specialities', SpecialityViewSet)
router.register(r'thirds', ThirdViewSet)

urls = router.urls