from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(False, null=True)
    
    