from django.http import HttpResponse
from django.shortcuts import redirect, render
from usuarios.models import Usuarios

from livro.models import Categoria, Emprestimos, Livros

from .forms import CadastroLivro, EmprestimoLivro, CategoriaLivro


def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id=request.session['usuario'])
        livros = Livros.objects.all()
        form_livro = CadastroLivro()
        form_emprestimo = EmprestimoLivro()
        form_categoria = CategoriaLivro()
        return render(request, 'home.html', {
            'livros': livros,
            'usuario_logado': request.session.get('usuario'),
            'form_livro': form_livro,
            'form_emprestimo': form_emprestimo,
            'form_categoria': form_categoria,
        })
    else:
        return redirect('/auth/login/?status=2')


def descricao(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id=id)
        categorias = Categoria.objects.all()
        emprestimo = Emprestimos.objects.filter(livro=livro)
        form_livro = CadastroLivro()
        form_emprestimo = EmprestimoLivro()
        form_categoria = CategoriaLivro()
        return render(request, 'descricao.html', {
            'livro': livro, 
            'categorias': categorias, 
            'emprestimo': emprestimo,
            'usuario_logado': request.session.get('usuario'),
            'form_livro': form_livro,
            'form_emprestimo': form_emprestimo,
            'form_categoria': form_categoria,
            'id_livro': id,
        })
    return redirect('/auth/login/?status=2')


def cadastrar(request):
    if request.method == "POST":
        form = CadastroLivro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/livro/home')
        else:
            return HttpResponse('DADOS INVÁLIDOS')


def excluir(request, id):
    livro = Livros.objects.get(id=id).delete()
    return redirect('/livro/home')


def cadastrar_categoria(request):
    form = CategoriaLivro(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    id_usuario = request.POST.get('usuario')
    if int(id_usuario) == int(request.session.get('usuario')):
        user = Usuarios.objects.get()
        categoria = Categoria(
            nome=nome, 
            descricao=descricao, 
            usuario=user, 
        )
        categoria.save()
        return redirect('/livro/home?cadastro_categoria=1')
    else:
        return HttpResponse('Pare de ser um usuário malandrinho. Não foi desta vez.')


def cadastrar_emprestimo(request):
    if request.method == 'POST':
        nome_emprestado = request.POST.get('nome_emprestado')
        nome_emprestado_anonimo = request.POST.get('nome_emprestado_anonimo')
        livro_emprestado = request.POST.get('livro_emprestado')
        
        if nome_emprestado_anonimo:
            emprestimo = Emprestimos(
                nome_emprestado_anonimo=nome_emprestado_anonimo,
                livro_id = livro_emprestado
            )
        else:
            emprestimo = Emprestimos(
                nome_emprestado_id=nome_emprestado,
                livro_id = livro_emprestado
            )
        emprestimo.save()

        livro = Livros.objects.get(id=livro_emprestado)
        livro.emprestado = True
        livro.save()


        return HttpResponse('Emprestimo realizado com sucesso')