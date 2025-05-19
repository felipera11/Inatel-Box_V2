# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.matricula = form.cleaned_data.get('matricula')
            user.username = str(user.matricula) 
            user.nome = form.cleaned_data.get('nome')
            user.email = form.cleaned_data.get('email')  # Save the email
            user.is_staff = form.cleaned_data.get('is_staff')  # Set staff status based on the checkbox
            user.save()
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Error occurred during signup.')
    else:
        form = SignUpForm()  # Use the custom signup form
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')