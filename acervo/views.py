from django.shortcuts import render, redirect
from .models import Livro, TIPO_CHOICES, CATEGORIA_CHOICES
from .forms import LivroForm


def lista_livros(request):
    livros = Livro.objects.all()

    nome = request.GET.get('nome')
    tipo = request.GET.get('tipo')
    categoria = request.GET.get('categoria')

    if nome:
        livros = livros.filter(titulo__icontains=nome)
    if tipo:
        livros = livros.filter(tipo=tipo)
    if categoria:
        livros = livros.filter(categoria=categoria)

    return render(
        request,
        'acervo/lista.html',
        {
            'livros': livros,
            'tipos': TIPO_CHOICES,
            'categorias': CATEGORIA_CHOICES,
            'nome_busca': nome or '',
            'tipo_busca': tipo or '',
            'categoria_busca': categoria or '',
        }
    )


def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista')

    else:
        form = LivroForm()

    return render(
        request,
        'acervo/form.html',
        {'form': form}
    )