from django.db import models
from apps.alunos.models import Aluno
from apps.livros.models import Livro
from datetime import date, timedelta

class Emprestimo(models.Model):
    aluno_id = models.ForeignKey(Aluno, verbose_name='Aluno', on_delete=models.CASCADE)
    livro_id = models.ForeignKey(Livro, verbose_name='Livro',on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(verbose_name='Data Empréstimo', auto_now_add=True)
    data_devolucao = models.DateField(verbose_name='Data Devolução', null=True, blank=True)
    data_prevista_devolucao = models.DateField(verbose_name='Previsão devolução', null=True, blank=True)
    status = models.CharField(max_length=1, choices=[('E','Emprestado'), ('D','Devolvido')])

    def __str__(self):
        return self.status

    def save(self, *args, **kwargs):
        # REGRA 1: Se for um novo registro, define valores iniciais
        if not self.id:
            if not self.status:  # Define como emprestado apenas se não houver status
                self.status = 'E'
            if not self.data_prevista_devolucao:
                self.data_prevista_devolucao = date.today() + timedelta(days=7)

        # REGRA 2: Vínculo da Data de Devolução com o Status
        # Se a data_devolucao estiver preenchida (não for None), muda status para 'D'
        if self.data_devolucao:
            self.status = 'D'
        else:
            # Caso a data seja apagada por algum motivo, ele volta a ser 'E'
            # ou se mantém 'E' enquanto não houver data de devolução
            self.status = 'E'

        super(Emprestimo, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Emprestimo'
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering = ['status']
        managed = True