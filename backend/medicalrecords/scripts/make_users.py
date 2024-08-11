from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from users.models import PermissionsSet, User

# We need to create a new permissions set for the medicalrecords app. One set by entity

for content_type in ContentType.objects.filter(app_label='medicalrecords').all():
    if PermissionsSet.objects.filter(content_type=content_type).exists():
        continue
    permissions_set = PermissionsSet.objects.create(path=content_type.model, content_type=content_type)
    permissions = Permission.objects.filter(content_type=content_type)
    permissions_set.permissions.set(permissions)
    permissions_set.save()

users_data = [
    {
        'username': "100100",
        'email': "victor@global.com",
        'password': "Admin2024",
        'first_name': "Victor",
        'last_name': "Hugo",
    },
    {
        'username': "100200",
        'email': "juan@global.com",
        'password': "Admin2024",
        'first_name': "Juan",
        'last_name': "Perez",
    },
    {
        'username': "100300",
        'email': "maria@global.com",
        'password': "Admin2024",
        'first_name': "Maria",
        'last_name': "Gomez",
    },
    {
        'username': "100400",
        'email': "maria@global.com",
        'password': "Admin2024",
        'first_name': "Juana",
        'last_name': "Gomez",
    },
    {
        'username': "100500",
        'email': "maria@global.com",
        'password': "Admin2024",
        'first_name': "Marta",
        'last_name': "Gomez",
    },
    {
        'username': "admin",
        'email': "admin@admin.com",
        'password': "Admin2024",
        'first_name': "Patricia",
        'last_name': "Admin",
    },
]



for user_data in users_data:
    User.objects.create_superuser(**user_data)
    
