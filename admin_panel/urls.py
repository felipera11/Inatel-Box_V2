from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('models/', views.admin_model_list, name='model_list'),
    path('models/<int:pk>/', views.admin_model_detail, name='model_detail'),
]
