
from .models import *
from .models import Cities, Diagnoses, Records, Specialities, Thirds
from django.contrib import admin

# Register your models here.

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    pass

@admin.register(Diagnoses)
class DiagnosesAdmin(admin.ModelAdmin):
    pass

@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
    pass

@admin.register(Specialities)
class SpecialitiesAdmin(admin.ModelAdmin):
    pass

@admin.register(Thirds)
class ThirdsAdmin(admin.ModelAdmin):
    pass




