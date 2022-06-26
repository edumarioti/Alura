
from django.shortcuts import render
from receitas.models import Receita

def busca(request):
    """ Realiza uma busca entre todas as receitas publicadas """
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        receitas_encontradas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
            
    dados = {
        'receitas' : receitas_encontradas
    }
    
    return render(request, 'receitas/buscar.html', dados)