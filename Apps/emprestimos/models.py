from django.db import models
from datetime import date
from Apps.alunos.models import Aluno
from Apps.livros.models import Livro

class Emprestimo(models.Model):
    id_Aluno = models.ForeignKey(Aluno, verbose_name='Aluno', on_delete=models.CASCADE)
    id_Livro = models.ForeignKey(Livro, verbose_name='Livro', on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(verbose_name='Data Empréstimo', auto_now_add=True)
    data_devolucao = models.DateField(verbose_name='Data Devolução', default=date.today)
    data_prevista_devolucao = models.DateField(verbose_name='Previsão devolução', default=date.today)
    status = models.CharField(max_length=1, choices=[('E', 'Emprestado'), ('D', 'Devolvido')])

    def __str__(self):
        return self.status

    class meta:
        db_table = 'emprestimos'
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering = ['status']
        managed = True