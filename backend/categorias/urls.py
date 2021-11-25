from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('descricao/<int:id>', views.descricao, name='descricao'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
    path('cadastrar_emprestimo/', views.cadastrar_emprestimo, name='cadastrar_emprestimo'),
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
]