from django.contrib import admin
from django.urls import path, include
from apps.core.views import index


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('alunos/', include('apps.alunos.urls', namespace='alunos')),
    path('livros/', include('apps.livros.urls', namespace='livros')),
    path('emprestimos/', include('apps.emprestimos.urls', namespace='emprestimos')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
