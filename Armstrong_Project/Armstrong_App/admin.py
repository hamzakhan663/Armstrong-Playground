from django.contrib import admin
from .models import ArmstrongUserProfile, UserAttempt

# Register your models here.
# Registered Models in the Database
admin.site.register(ArmstrongUserProfile)
admin.site.register(UserAttempt)
