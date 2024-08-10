from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    """ This is our custom user model that we will use to authenticate users """
    
    USERNAME_FIELD = 'email'