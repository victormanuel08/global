from django.contrib import admin
from django.urls import path, include
from medicalrecords import urls as medicalrecords_urls

urlpatterns = [
    path('admin/', admin.site.urls),    
    # path('', include(medicalrecords_urls)) ## Acá no hay ninguna url para importar como está
]

