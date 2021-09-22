from django.contrib import admin
from .models import (TbAluno, TbDoacao, TbDoacaoItem,
                     TbEmprestimo, TbFuncionario, TbGenero,
                     TbLivro, TbParteleira, TbUsuario)


# Register your models here.
@admin.register(TbAluno)
class TbAlunoAdmin(admin.ModelAdmin):
    list_display = ('alu_id', 'alu_nome', 'alu_ra', 'alu_email',
                    'alu_usu', 'alu_dtcastro', 'alu_ativo')


@admin.register(TbDoacao)
class TbDoacaoAdmin(admin.ModelAdmin):
    pass


@admin.register(TbDoacaoItem)
class TbDoacaoItemAdmin(admin.ModelAdmin):
    pass


@admin.register(TbEmprestimo)
class TbEmprestimoAdmin(admin.ModelAdmin):
    pass


@admin.register(TbFuncionario)
class TbFuncionarioAdmin(admin.ModelAdmin):
    pass


@admin.register(TbGenero)
class TbGeneroAdmin(admin.ModelAdmin):
    pass


@admin.register(TbLivro)
class TbLivroAdmin(model.ModelAdmin):
    pass


@admin.register(TbParteleira)
class TbParteleiraAdmin(model.ModelAdmin):
    pass


admin.site.register(TbUsuario)
