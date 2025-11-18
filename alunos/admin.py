from django.contrib import admin
from .models import (Aluno)


# Register your models here.

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'email', 'telefone', 'data_evento')
    search_fields = ('nome', 'matricula', 'data_evento')


from django.contrib import admin

# Register your models here.
