# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Importa o modelo correto

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField(required=False, label='Criar como administrador')

    class Meta:
        model = CustomUser
        fields = ['matricula', 'nome', 'email', 'password1', 'password2', 'is_staff']