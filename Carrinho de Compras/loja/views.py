from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def loja(request):
    lista_produtos = Produto.objects.all()
    context = {
        'titulo': 'Minha Loja Bonita',
        'usuario': 'Jorge',
        'lista': lista_produtos,
    }
    return render(request, 'loja.html', context)

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = request.session.get('carrinho', {})

    if str(produto_id) in carrinho:
        carrinho[str(produto_id)]['quantidade'] += 1
    else:

        carrinho[str(produto_id)] = {
            'nome': produto.nome,
            'preco': str(produto.preco),
            'quantidade': 1
        }
    
    request.session['carrinho'] = carrinho
    
    return redirect('loja_principal')

def carrinho(request):
    carrinho_da_sessao = request.session.get('carrinho', {})
    carrinho_itens = []
    total = 0

    for item_id, item_data in carrinho_da_sessao.items():
        subtotal = float(item_data['preco']) * item_data['quantidade']
        total += subtotal
        carrinho_itens.append({
            'id': item_id,
            'nome': item_data['nome'],
            'preco': item_data['preco'],
            'quantidade': item_data['quantidade'],
            'subtotal': subtotal
        })

    context = {
        'carrinho_itens': carrinho_itens,
        'total': total
    }
    return render(request, 'carrinho.html', context)

def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})

    if str(produto_id) in carrinho:
        del carrinho[str(produto_id)]
        request.session['carrinho'] = carrinho

    return redirect('ver_carrinho')