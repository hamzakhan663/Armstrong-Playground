from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ArmstrongUserProfile

class ArmstrongUserProfileForm(forms.Form):
    name = forms.CharField(max_length=255)
    contact_number = forms.CharField(max_length=15)
    class Meta:
        model = ArmstrongUserProfile
        fields = ['name','contact_number']

    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']