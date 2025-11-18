from django.contrib import admin
from .models import Livro, Aluno, Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_Aluno', 'id_Livro', 'data_emprestimo', 'status')
    search_fields = ['data_emprestimo', 'status']