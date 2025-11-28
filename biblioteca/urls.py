from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Apps.core.urls')),
    path('alunos/', include('Apps.alunos.urls')),
    path('emprestimos/', include('Apps.emprestimos.urls')),
]
