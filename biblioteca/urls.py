from django.contrib import admin
from django.urls import path, include
from apps.core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # Inclui todas as URLs do app alunos sob o prefixo '/alunos/'
    path('alunos/', include('apps.alunos.urls', namespace='alunos')),
    path('livros/', include('apps.livros.urls', namespace='livros')),
]