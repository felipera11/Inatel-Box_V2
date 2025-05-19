from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    COMPONENTE = 'componente'
    FERRAMENTA = 'ferramenta'
    CATEGORIA_CHOICES = [
        (COMPONENTE, 'Componente'),
        (FERRAMENTA, 'Ferramenta'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    categoria = models.CharField(max_length=100, null=False, default="Geral")
    quantidade = models.PositiveIntegerField(default=0)
    unidade = models.CharField(max_length=20, default="un")  # ex: un, kg, m

    def __str__(self):
        return f"{self.nome} ({self.quantidade} {self.unidade})"

class RegistroMovimentacao(models.Model):
    ENTRADA = 'entrada'
    SAIDA = 'saida'

    TIPO_CHOICES = [
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField()
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True)
    emprestimo_de = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='emprestimos')

    def __str__(self):
        return f"{self.tipo.title()} - {self.produto.nome} ({self.quantidade})"
