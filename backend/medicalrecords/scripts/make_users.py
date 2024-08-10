from users.models import User

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
        'first_name': "Maria",
        'last_name': "Gomez",
    },
    {
        'username': "100500",
        'email': "maria@global.com",
        'password': "Admin2024",
        'first_name': "Maria",
        'last_name': "Gomez",
    },
    {
        'username': "admin",
        'email': "admin@admin.com",
        'password': "Admin2024",
        'first_name': "Admin",
        'last_name': "Admin",
    },
]

for user_data in users_data:
    User.objects.create_superuser(**user_data)
    
print("Users created successfully")
