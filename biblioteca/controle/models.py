# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbAluno(models.Model):
    alu_id = models.AutoField(primary_key=True)
    alu_nome = models.TextField()
    alu_ra = models.IntegerField()
    alu_email = models.TextField(blank=True, null=True)
    alu_usu = models.ForeignKey('TbUsuario', models.DO_NOTHING, blank=True, null=True)
    alu_dtcastro = models.DateTimeField()
    alu_ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_aluno'


class TbDoacao(models.Model):
    doa_id = models.AutoField(primary_key=True)
    doa_descricao = models.TextField(blank=True, null=True)
    doa_doador = models.TextField()
    doa_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_doacao'


class TbDoacaoItem(models.Model):
    doi_id = models.AutoField(primary_key=True)
    doi_doa = models.ForeignKey(TbDoacao, models.DO_NOTHING, blank=True, null=True)
    doi_titulo = models.TextField(blank=True, null=True)
    doi_gen_id = models.TextField()
    doi_qnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_doacao_item'


class TbEmprestimo(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_lvr = models.ForeignKey('TbLivro', models.DO_NOTHING)
    emp_alu = models.ForeignKey(TbAluno, models.DO_NOTHING, blank=True, null=True)
    emp_fun = models.ForeignKey('TbFuncionario', models.DO_NOTHING, blank=True, null=True)
    emp_dt_prevdev = models.DateField()
    emp_dt_dev = models.DateTimeField()
    emp_qnt = models.IntegerField(blank=True, null=True)
    emp_dt = models.DateTimeField()
    emp_usu_cad = models.IntegerField()
    emp_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_emprestimo'


class TbFuncionario(models.Model):
    fun_id = models.AutoField(primary_key=True)
    fun_nome = models.TextField()
    fun_cargo = models.TextField()
    fun_email = models.TextField()
    fun_usu = models.ForeignKey('TbUsuario', models.DO_NOTHING)
    fun_dtcastro = models.DateTimeField()
    fun_ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_funcionario'


class TbGenero(models.Model):
    gen_id = models.AutoField(primary_key=True)
    gen_descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_genero'


class TbLivro(models.Model):
    lvr_id = models.AutoField(primary_key=True)
    lvr_titulo = models.TextField(blank=True, null=True)
    lvr_gen = models.ForeignKey(TbGenero, models.DO_NOTHING, blank=True, null=True)
    lvr_autor = models.TextField(blank=True, null=True)
    lvr_qnt = models.TextField(blank=True, null=True)
    lvr_partimonio = models.IntegerField(blank=True, null=True)
    lvr_doacao = models.IntegerField(blank=True, null=True)
    lvr_dtcastro = models.DateTimeField()
    lvr_par = models.ForeignKey('TbParteleira', models.DO_NOTHING)
    lvr_part_local = models.TextField(blank=True, null=True)
    lvr_ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_livro'


class TbParteleira(models.Model):
    par_id = models.AutoField(primary_key=True)
    par_rua = models.TextField(blank=True, null=True)
    par_altura = models.TextField(blank=True, null=True)
    par_largura = models.TextField(blank=True, null=True)
    par_descricao = models.TextField(blank=True, null=True)
    par_usu_cadastro = models.IntegerField(blank=True, null=True)
    par_dtcastro = models.DateTimeField()
    par_ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tb_parteleira'


class TbUsuario(models.Model):
    usu_id = models.AutoField(primary_key=True)
    usu_nome = models.TextField()
    usu_nome_completo = models.TextField()
    usu_email = models.TextField()
    usu_tipo = models.TextField(blank=True, null=True)
    usu_senha = models.TextField()
    usu_ativo = models.BooleanField()
    usu_dtcastro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tb_usuario'
