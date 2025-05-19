# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),  # Ensure this line exists and is named 'home'
    path('send_model/', views.send_model, name='send_model'),
    path('history/', views.history, name='history'),
    path('model/<int:pk>/', views.print_model_detail, name='print_model_detail'),
]
