from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey
from usuarios.models import Usuarios


class Categoria(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, default=None)
    
    
    def __str__(self):
        return self.nome
    
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Livros(models.Model):
    titulo = models.CharField(max_length=128)
    autor = models.CharField(max_length=64)
    co_autor = models.CharField(max_length=64, null=True, blank=True)
    editora = models.CharField(max_length=32, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)
    quantidade = models.PositiveIntegerField()
    partimonio = models.CharField(max_length=32)
    ativo = models.BooleanField()
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, default=None)
    usuarios = models.ForeignKey(Usuarios, on_delete=DO_NOTHING, default=None)


    def __str__(self):
        return f'{self.titulo} | {self.autor}'


    class Meta:
        db_table = 'Tabela do Livro'
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'


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