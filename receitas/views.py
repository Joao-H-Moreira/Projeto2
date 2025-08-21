from django.shortcuts import render, get_list_or_404
from .models import Receita


# receitas/views.py 

def home(request): 
    return render(request, 'receitas/home.html') 

def receita_detail(request, id):

    receita = get_list_or_404(Receita, pk=id)

    context = {
        'receita' : receita,

    }

    return render(request, 'receitas/receita_detail.html', context)
    
