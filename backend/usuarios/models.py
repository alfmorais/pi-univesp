from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField()
    senha = models.CharField(max_length=64)


    def __str__(self):
        return self.nome


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'