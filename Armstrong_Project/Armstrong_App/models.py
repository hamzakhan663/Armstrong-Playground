from django.db import models
from django.contrib.auth.models import User



# Create your models here.    
class ArmstrongUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

class UserAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    attempt_type = models.CharField(max_length=255)  # e.g., 'Searching Range' or 'Checking Single Number'
    attempt_value = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    

