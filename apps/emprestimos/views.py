from django.contrib import messages
from django.db.models.functions import Lower

from .forms import EmprestimoForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Emprestimo

def inserir_emprestimo(request):
    template_name = 'emprestimos/form_emprestimo.html'
    if request.method == 'POST':
        form = EmprestimoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro do Emprestimo foi realizado com sucesso!')
        return redirect('emprestimos:listar_emprestimos')
    form = EmprestimoForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_emprestimos(request):
    template_name = 'emprestimos/listar_emprestimos.html'

    ordem = request.GET.get('ordem', 'id_asc')  # padrão

    if ordem == 'aluno_asc':
        emprestimos = Emprestimo.objects.all().order_by(Lower('aluno_id'))
    elif ordem == 'aluno_desc':
        emprestimos = Emprestimo.objects.all().order_by(Lower('aluno_id').desc())
    elif ordem == 'id_asc':
        emprestimos = Emprestimo.objects.all().order_by('id')
    elif ordem == 'id_desc':
        emprestimos = Emprestimo.objects.all().order_by('-id')
    elif ordem == 'livro_id_asc':
        emprestimos = Emprestimo.objects.all().order_by(Lower('livro_id'))
    elif ordem == 'livro_id_desc':
        emprestimos = Emprestimo.objects.all().order_by(Lower('livro_id').desc())
    else:
        emprestimos = Emprestimo.objects.all().order_by('id')

    context = {
        'emprestimos': emprestimos,
        'ordem': ordem,
    }
    return render(request, template_name, context)

def editar_emprestimo(request, id):
    template_name = 'emprestimos/editar_emprestimo.html'
    emprestimo = get_object_or_404(Emprestimo, id=id)
    form = EmprestimoForm(request.POST or None, request.FILES or None, instance=emprestimo)
    context = {'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
        return redirect('emprestimos:listar_emprestimos')
    return render(request, template_name, context)

def excluir_emprestimo(request, id):
    template_name = 'emprestimos/excluir_emprestimo.html'
    emprestimo = Emprestimo.objects.get(id=id)
    context = {'emprestimo': emprestimo}
    if request.method == "POST":
        emprestimo.delete()
        messages.error(request, 'O Emprestimo foi excluído com sucesso.')
        return redirect('emprestimos:listar_emprestimos')
    return render(request, template_name, context)

def status_emprestimo(request, id):
    template_name = 'emprestimos/status_emprestimo.html'
    emprestimo = Emprestimo.objects.get(id=id)
    context = {'emprestimo': emprestimo}
    return render(request, template_name, context)