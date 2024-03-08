from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArmstrongUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
