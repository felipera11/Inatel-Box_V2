# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),  # Ensure this line exists and is named 'home'
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('movimentar/', views.movimentar_produto, name='movimentar_produto'),
]
