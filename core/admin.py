from django.contrib import admin
from .models import Produto, Categoria, RegistroMovimentacao

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(RegistroMovimentacao)
