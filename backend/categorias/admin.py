from django.contrib import admin
from livro.models import Livros, Categoria, Emprestimos


# Register your models here.
@admin.register(Livros)
class LivrosAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
        'autor',
        'co_autor',
        'editora',
        'data_cadastro',
        'emprestado',
        'quantidade',
        'patrimonio',
        'ativo',
    ]


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        "nome", 
        "descricao",
    ]


@admin.register(Emprestimos)
class EmprestimosAdmin(admin.ModelAdmin):
    list_display = [
        "nome_emprestado", 
        "data_emprestimo",
        "data_devolucao",
        "tempo_duracao",
        "livro",
    ]