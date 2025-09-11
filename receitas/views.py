from django.shortcuts import render, get_object_or_404
from .models import Receita

# receitas/views.py 
def home(request): 
    categoria_slug = request.GET.get('categoria')
    categorias_choices = [choice[0] for choice in Receita.CATEGORIAS]
    if categoria_slug:
        receitas = Receita.objects.filter(categoria=categoria_slug)
        categoria_selecionada = categoria_slug
    else:
        receitas = Receita.objects.all()
        categoria_selecionada = None
        
    return render(request, 'receitas/home.html', {'receitas':receitas, 'categoria': categorias_choices, 'categoria_selecionada': categoria_selecionada}) 

def receita_detail(request, id):
    receita = get_object_or_404(Receita, pk=id)
    return render(request, 'receitas/receita_detail.html', {'receita': receita})

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