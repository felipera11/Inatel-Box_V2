# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    is_staff = forms.BooleanField(required=False, label='Create as staff user')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2', 'is_staff']
