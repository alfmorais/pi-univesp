from django.contrib import admin
from .models import Usuarios


@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    readonly_fields = (
        'nome',
        'email',
        'senha',
    )
    list_display = [
        'nome',
        'email',
        'senha',
    ]
