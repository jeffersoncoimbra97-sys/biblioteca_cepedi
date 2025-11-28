from django.contrib import admin
from .models import (Livro)
# Register your models here.

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'edicao')
    search_fields = ('titulo', 'autor')