CREATE TABLE tb_usuario (
	usu_id serial NOT NULL,
	usu_nome TEXT NOT NULL,
	usu_nome_completo TEXT NOT NULL,
	usu_email TEXT NOT NULL,
	usu_tipo TEXT NULL,
    usu_senha TEXT NOT NULL,
    usu_ativo BOOLEAN NOT NULL DEFAULT FALSE,
    usu_dtcastro TIMESTAMP NOT NULL,
    CONSTRAINT tb_usuario_usu_id_pk PRIMARY KEY (usu_id)
    );

CREATE TABLE tb_funcionario (
	fun_id serial NOT NULL,
	fun_nome TEXT NOT NULL,
	fun_cargo TEXT NOT NULL,
	fun_email TEXT NOT NULL,
	fun_usu_id INT4 NOT NULL, 
    fun_dtcastro TIMESTAMP NOT NULL, 
    fun_ativo BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT tb_funcionaio_fun_id_pk PRIMARY KEY (fun_id),
    CONSTRAINT tb_funcionaio_fun_usu_id_fk FOREIGN KEY (fun_usu_id) REFERENCES tb_usuario(usu_id)
);
CREATE TABLE tb_aluno (
	alu_id serial NOT NULL,
	alu_nome TEXT NOT NULL,
	alu_ra INT4 NOT NULL,
	alu_email TEXT NULL,
	alu_usu_id INT4 NULL, 
    alu_dtcastro TIMESTAMP NOT NULL, 
    alu_ativo BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT pk_tb_aluno_alu_id_pk PRIMARY KEY (alu_id),
    CONSTRAINT tb_aluno_alu_usu_id_fk FOREIGN KEY (alu_usu_id) REFERENCES tb_usuario (usu_id)
);

CREATE TABLE tb_parteleira (
	par_id serial NOT NULL,
	par_rua TEXT NULL,	
	par_altura TEXT NULL,
	par_largura TEXT NULL,
	par_descricao TEXT NULL,
	par_usu_cadastro INT4  NULL, 
    par_dtcastro TIMESTAMP NOT NULL, 
    par_ativo BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT tb_parteleira_par_id_pk PRIMARY KEY (par_id)
);

CREATE TABLE tb_genero (
	gen_id serial NOT NULL,
	gen_descricao TEXT NULL,
    CONSTRAINT tb_genero_gen_id_pk PRIMARY KEY (gen_id)
);

CREATE TABLE tb_doacao (
	doa_id serial NOT NULL,
	doa_descricao TEXT NULL,
	doa_doador TEXT NOT NULL,
	doa_dt TIMESTAMP NOT NULL ,
    CONSTRAINT tb_doacao_doa_id_pk PRIMARY KEY (doa_id)
);

CREATE TABLE tb_doacao_item (
	doi_id serial NOT NULL,
	doi_doa_id INT4 NULL,
	doi_titulo TEXT NULL,
	doi_gen_id TEXT NOT NULL,
	doi_qnt INT4 NULL,
    CONSTRAINT tb_doacao_item_doi_id_pk PRIMARY KEY (doi_id),
    CONSTRAINT tb_doacao_item_doi_doa_id_fk FOREIGN KEY (doi_doa_id) REFERENCES tb_doacao (doa_id)
);
CREATE TABLE tb_livro (
	lvr_id serial NOT NULL,
	lvr_titulo TEXT NULL,
	lvr_gen_id INT4 NULL,	
	lvr_autor TEXT NULL,
	lvr_qnt TEXT NULL,
	lvr_partimonio INT4 NULL,
	lvr_doacao INT4  NULL, 
    lvr_dtcastro TIMESTAMP NOT NULL , 
    lvr_par_id INT4 NOT NULL,
    lvr_part_local TEXT NULL,
    lvr_ativo BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT tb_livro_lvr_id_pk PRIMARY KEY (lvr_id),
    CONSTRAINT tb_livro_lvr_gen_id_fk FOREIGN KEY (lvr_gen_id) REFERENCES tb_genero(gen_id)
);

CREATE TABLE tb_emprestimo (
	emp_id serial NOT NULL,
	emp_lvr_id INT4 NOT NULL,
	emp_alu_id INT4 NULL,
	emp_fun_id INT4 NULL,
	emp_dt_prevdev DATE NOT NULL,
	emp_dt_dev TIMESTAMP NOT NULL,	
	emp_qnt INT4 NULL,
	emp_dt TIMESTAMP NOT NULL,
	emp_usu_cad INT4 NOT NULL,
	emp_status VARCHAR(1) NULL,
    CONSTRAINT tb_emprestimo_emp_id_pk PRIMARY KEY (emp_id),
    CONSTRAINT tb_emprestimo_emp_lvr_id_fk FOREIGN KEY (emp_lvr_id) REFERENCES tb_livro (lvr_id),
    CONSTRAINT tb_emprestimo_emp_alu_id_fk FOREIGN KEY (emp_alu_id) REFERENCES tb_aluno (alu_id),
    CONSTRAINT tb_emprestimo_emp_fun_id_fk FOREIGN KEY (emp_fun_id) REFERENCES tb_funcionario (fun_id)
);