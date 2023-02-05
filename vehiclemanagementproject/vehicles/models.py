from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_user= models.BooleanField('Is user', default=False)
    is_admin = models.BooleanField('Is admin', default=False)
    is_superadmin = models.BooleanField('Is superuser', default=False)


class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('TW', 'Two-Wheeler'),
        ('TW', 'Three-Wheeler'),
        ('FW', 'Four-Wheeler')
    ]

    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=2, choices=VEHICLE_TYPE_CHOICES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField(blank=True)

    def __str__(self):
        return self.vehicle_number