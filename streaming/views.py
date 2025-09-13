from django.shortcuts import render,redirect
from .forms import FilmeForm
from .models import Filmes

def cadastrar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')  # depois a gente cria essa rota
    else:
        form = FilmeForm()
    
    return render(request, 'filmes/cadastrar.html', {'form': form})

def listar_filmes(request):
    busca = request.GET.get('q')
    if busca:
        filmes = Filmes.objects.filter(titulo__icontains=busca)
    else:
        filmes = Filmes.objects.all()
    return render(request, 'filmes/listar.html', {'filmes': filmes})

