# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'username', 'email', 
            'profile_picture', 'password1', 'password2', 
            'address_line1', 'city', 'state', 'pincode', 
            'is_patient', 'is_doctor'
        )
