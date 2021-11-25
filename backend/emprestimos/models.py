from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey
from usuarios.models import Usuarios
from livro.models import Livros

class Emprestimos(models.Model):
    nome_emprestado = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)


    def __str__(self):
        return f'{self.nome_emprestado} pegou o livro no dia {self.data_emprestimo}.'
    
    
    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'