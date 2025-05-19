# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto, RegistroMovimentacao
from .forms import ProdutoForm, RegistroMovimentacaoForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'core/listar_produtos.html', {'produtos': produtos})

@login_required
@user_passes_test(is_admin)
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

            produto = movimentacao.produto

            if movimentacao.tipo == 'entrada':
                # Verifica se o usuário pode devolver
                emprestimos_ativos = RegistroMovimentacao.objects.filter(
                    produto=produto,
                    tipo='saida',
                    emprestimo_de=request.user
                ).exists()

                if not emprestimos_ativos:
                    form.add_error(None, "Você não possui esse produto emprestado para devolvê-lo.")
                    return render(request, 'core/movimentar_produto.html', {'form': form})

                produto.quantidade += movimentacao.quantidade

            else:  # Saída
                if produto.quantidade < movimentacao.quantidade:
                    form.add_error(None, "Quantidade insuficiente para empréstimo.")
                    return render(request, 'core/movimentar_produto.html', {'form': form})
                produto.quantidade -= movimentacao.quantidade
                movimentacao.emprestimo_de = request.user  # Marca quem pegou emprestado

            produto.save()
            movimentacao.save()
            return redirect('core:listar_produtos')
    else:
        form = RegistroMovimentacaoForm()
    return render(request, 'core/movimentar_produto.html', {'form': form})

@login_required
def meus_emprestimos(request):
    # Filtra todas as saídas feitas pelo usuário atual
    saidas = RegistroMovimentacao.objects.filter(
        tipo='saida',
        emprestimo_de=request.user
    )

    # Para cada produto emprestado, subtrai entradas devolvidas
    emprestimos = []
    for saida in saidas:
        devolucoes = RegistroMovimentacao.objects.filter(
            tipo='entrada',
            produto=saida.produto,
            responsavel=request.user
        ).aggregate(total=Sum('quantidade'))['total'] or 0

        restante = saida.quantidade - devolucoes
        if restante > 0:
            emprestimos.append({
                'produto': saida.produto,
                'quantidade': restante,
                'unidade': saida.produto.unidade
            })

    return render(request, 'core/meus_emprestimos.html', {'emprestimos': emprestimos})

