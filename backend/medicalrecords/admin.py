
from .models import *
from .models import Services, Procedures, Records_details, Availability, Cities, Diagnoses, Records, Specialities, Thirds, Scheduled, SEX_CHOICES,TYPE_CHOICES, BLOOD_CHOICES, MATERNITY_PREGNANCY_CHOICES, MATERNITY_BREASFEEDING_CHOICES, MATERNITY_BREASFEEDING_EXTEND_CHOICES, MATERNITY_BREASFEEDING_COMPLEMENTARY_CHOICES, MATERNITY_VIOLANCE_CHOICES
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
    readonly_fields = ('diagnosis', 'diagnosis_1', 'diagnosis_2', 'diagnosis_3')

@admin.register(Records_details)
class Records_detailsAdmin(admin.ModelAdmin):
    pass

@admin.register(Specialities)
class SpecialitiesAdmin(admin.ModelAdmin):
    pass

@admin.register(Thirds)
class ThirdsAdmin(admin.ModelAdmin):
    pass

@admin.register(Scheduled)
class ScheduledAdmin(admin.ModelAdmin):
    pass

@admin.register(GeneralExam)
class GeneralExamAdmin(admin.ModelAdmin):
    pass

@admin.register(SystemsReview)
class SystemsReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    pass

@admin.register(Procedures)
class ProceduresAdmin(admin.ModelAdmin):
    pass

@admin.register(Vehicles)
class VehicleAdmin(admin.ModelAdmin):
    pass

@admin.register(Policy)
class PoliceAdmin(admin.ModelAdmin):
    pass

@admin.register(Fees)
class FeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    pass

