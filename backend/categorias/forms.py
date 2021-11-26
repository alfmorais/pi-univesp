from django import forms
from .models import Livros, Categoria, Emprestimos

class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livros
        fields = (
            "titulo",
            "autor",
            "co_autor",
            "editora",
            "emprestado",
            "quantidade",
            "patrimonio",
            "ativo",
            "categoria",
            "usuarios",
        )


class CategoriaLivro(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = (
            "nome",
            "descricao",
            "usuario",
        )


class EmprestimoLivro(forms.ModelForm):
    class Meta:
        model = Emprestimos
        fields = (
            "nome_emprestado",
            "data_emprestimo",
            "data_devolucao",
            "tempo_duracao",
            "livro",
        )