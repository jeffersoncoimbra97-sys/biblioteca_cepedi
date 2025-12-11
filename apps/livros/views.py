from django.contrib import messages

from .forms import LivroForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro

def inserir_livro(request):
    template_name = 'livros/form_livros.html'
    if request.method == 'POST':
        form = LivroForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro do Livro foi realizado com sucesso!')
        return redirect('livros:listar_livros')
    form = LivroForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_livros(request):
    template_name = 'livros/listar_livros.html'
    livros = Livro.objects.all()
    context = {'relacao_livros': livros}
    return render(request, template_name, context)


def editar_livro(request, id):
    template_name = 'livros/form_livros.html'
    livro = get_object_or_404(Livro, id=id)
    form = LivroForm(request.POST or None, request.FILES or None, instance=livro)
    context = {'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
        return redirect('livros:editar_livro')
    return render(request, template_name, context)

def excluir_livro(request, id):
    template_name = 'livros/excluir_livro.html'
    livro = Livro.objects.get(id=id)
    context = {'livro': livro}
    if request.method == "POST":
        livro.delete()
        messages.error(request, 'O livro foi excluído com sucesso.')
        return redirect('livros:listar_livros')
    return render(request, template_name, context)