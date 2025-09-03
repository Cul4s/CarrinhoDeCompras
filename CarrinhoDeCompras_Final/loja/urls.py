from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loja, name='loja_principal'),
    path('produto/<int:produto_id>/', views.produto_detalhe, name='produto_detalhe'),
    path('produto/<int:produto_id>/adicionar/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', views.carrinho, name='ver_carrinho'),
    path('carrinho/remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]