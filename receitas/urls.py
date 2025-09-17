from django.urls import path 
from . import views 

urlpatterns = [ 
path('', views.home, name='home'), 
path('sibre_nos/', views.sobre_nos, name='sobre_nos'),
path('receita/<int:id>/', views.receita_detail, name='receita_detail'),
path('pesquisar/', views.pesquisar_receitas, name='pesquisar_receitas'),
path('contato/', views.contato, name='contato' ),
path('sucesso/', views.sucesso, name='sucesso' ),
] 