# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto, RegistroMovimentacao
from .forms import ProdutoForm, RegistroMovimentacaoForm

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'core/listar_produtos.html', {'produtos': produtos})

@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'core/adicionar_produto.html', {'form': form})

@login_required
def movimentar_produto(request):
    if request.method == 'POST':
        form = RegistroMovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.responsavel = request.user
            movimentacao.save()

            produto = movimentacao.produto
            if movimentacao.tipo == 'entrada':
                produto.quantidade += movimentacao.quantidade
            else:
                produto.quantidade -= movimentacao.quantidade
            produto.save()

            return redirect('core:listar_produtos')
    else:
        form = RegistroMovimentacaoForm()
    return render(request, 'core/movimentar_produto.html', {'form': form})