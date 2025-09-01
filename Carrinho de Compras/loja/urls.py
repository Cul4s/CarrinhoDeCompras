from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loja, name='loja_principal'),
    path('carrinho/', views.carrinho, name='ver_carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]