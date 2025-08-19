from django.shortcuts import render
from django.http import Http404

# receitas/views.py 

def home(request): 
    return render(request, 'receitas/home.html') 

def receita_detail(request, id):

    context = {
        'receita_id' : id,
        'receita_title' : f'Receita detalhada {id}',
        'receita_desciption' : f'Esta é a descrição detalhada da receita com ID {id}.'
    }
    
