from django.contrib import admin
from .models import ArmstrongUserProfile, UserAttempt

# Register your models here.
admin.site.register(ArmstrongUserProfile)
admin.site.register(UserAttempt)