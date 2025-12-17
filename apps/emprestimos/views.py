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

    ordem = request.GET.get('ordem', 'titulo_asc')  # padrão

    if ordem == 'id_asc':
        emprestimos = emprestimo.objects.all().order_by('id')
    elif ordem == 'id_desc':
        emprestimos = emprestimo.objects.all().order_by('-id')
    elif ordem == 'aluno_asc':
        emprestimos = emprestimo.objects.all().order_by(Lower('aluno_id'))
    elif ordem == 'aluno_desc':
        emprestimos = emprestimo.objects.all().order_by(Lower('aluno_id').desc())
    elif ordem == 'titulo_asc':
        emprestimos = emprestimo.objects.all().order_by(Lower('titulo_id'))
    elif ordem == 'titulo_desc':
        emprestimos = emprestimo.objects.all().order_by(Lower('titulo_id').desc())
    else:
        emprestimos = emprestimo.objects.all().order_by(Lower('id'))  # fallback

    context = {
        'emprestimos': emprestimos,
        'ordem': ordem,
    }
    return render(request, template_name, context)
