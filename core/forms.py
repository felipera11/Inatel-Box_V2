from django import forms
from .models import Produto, RegistroMovimentacao

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categoria', 'quantidade', 'unidade']

class RegistroMovimentacaoForm(forms.ModelForm):
    class Meta:
        model = RegistroMovimentacao
        fields = ['produto', 'tipo', 'quantidade', 'observacao']
