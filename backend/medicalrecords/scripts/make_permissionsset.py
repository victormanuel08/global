from users.models import PermissionsSet
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# We need to create a new permissions set for the medicalrecords app. One set by entity

print("Creating permissions sets for medicalrecords app", len(ContentType.objects.filter(app_label='medicalrecords')))

for model in ContentType.objects.filter(app_label='medicalrecords').all():
    print("Hola", model)
    permissions_set = PermissionsSet.objects.create(path=model.model)
    permissions = Permission.objects.filter(content_type=model)
    permissions_set.permissions.set(permissions)
    permissions_set.save()
    print(f"Permissions set for {model.model} created")
    
print("Permissions sets created successfully")

