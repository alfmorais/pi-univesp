from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey
from usuarios.models import Usuarios

class Categoria(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.CharField(max_length=128)
    usuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING, default=None)
    
    
    def __str__(self):
        return self.nome
    
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

