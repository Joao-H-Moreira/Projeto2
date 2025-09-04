from django.shortcuts import render, get_object_or_404
from .models import Receita

# receitas/views.py 
def home(request): 
    receitas = Receita.objects.all()
    return render(request, 'receitas/home.html', {'receitas':receitas}) 

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)
    
    context = {
        'receita': receita,
    }
    return render(request, 'receitas/receita_detail.html', context)

def pesquisar_receitas(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Receita.objects.filter(title__icontains=query)
    
    context = {
        'query': query,
        'resultados': resultados,
    }
    
    return render(request, 'receitas/pesquisa.html', context)