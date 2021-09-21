# Django - Passo a Passo

## 1° Ambiente Virtual

Sempre quando iniciar um projeto, devemos isolar esse ambiente de desenvolvimento do nosso equipamento (computador). Isso ajuda a manter a estabilidade do sistema e evitar conflito de versões de bibliotecas. 

Exemplo: Na sua máquina você utiliza o Python versão 2.7. Mas, no projeto da biblioteca, vamos utilizar o Python na última versão 3.9.5. O ambiente evita esses tipos de conflitos.

Criando um ambiente virtual:

~~~cmd
python -m venv library
~~~

Descrevendo o comando:

1. python -m venv -> O comando python para criar um ambiente virtual.
2. library -> O nome do ambiente virtual. 

Ativando o ambiente virtual:

~~~cmd
library/Scripts/Activate
~~~

A palavra library vai aparecer na frente da sua linha de comando entre-parenteses. 

_imagem_

## 2° Instalando o Django e o PostgreSQL

Para instalar o Django e o PostgreSQL usaremos os seguintes códigos no terminal do Windows: 

~~~cmd
pip install django
~~~

Para rodar Postgres rodar com o Django vamos precisar de um driver também, chamado psycopg2.

~~~cmd
pip install psycopg2
~~~

## 3° Iniciando o projeto Django

Com o ambiente virtual inciado e as depedências instaladas, vamos inciar o nosso projeto. 

~~~cmd
django-admin startproject myproject
~~~

Vamos verificar se o Django está funcionando corretamente. 

~~~cmd
python manage.py runserver
~~~

## 4° Configurando o PostgreSQL no Django

Como o Django por padrão vem setado para o SQLite temos que alterar as configs para o PostgreSQL.
Proseguindo, abra o arquivo settings.py e deixe a constante DATABASES deste jeito:

~~~python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'root',
        'PASSWORD': 'Den.11101',
        'HOST': 'db',
        'PORT': 5432,
    }
}
~~~

## 5° Criando o Super User

Com o comando abaixo criaremos nosso usuário para usar a área administrativa:

~~~cmd
python manage.py createsuperuser
~~~

nome:

e-mail:

senha: 

Digite seu usário e senha e não se esqueça destas credenciais, vamos utilizar mais adiante

## 6° Migrações Padrões do Django e "Hello World!"

O Django vem com um admin pronto e uma estrutura de usuários e hierarquia, basta rodar o comando abaixo para fazer todas as migrações:

~~~cmd
python manage.py migrate
~~~

## 7° Acessando o painel administrativo do Django

Acessando o painel admin do Django: 

~~~cmd
python manage.py runserver
~~~

1. Clica no link de Localhost
2. Vai até a URL do Google Chrome que abriu e digite o seguinte endereço: <b>http://localhost:8080/admin</b>
3. Insira o usuário e a senha definido no passo 5. 

_imagem_

## 8° Fazendo a migração do banco legado no Django
## 9° Configurando a view da tela inicial
## 10° Inserindo o usuário na tela de Login
## 11° Após o login: Tela do Sistema!
## 12°

## Referências
1. [Documentação do Django](https://docs.djangoproject.com/pt-br/3.2/)
2. [Integrando Django com PostgreSQL ( Windows e Linux )](https://www.horadecodar.com.br/2019/01/24/integrando-django-com-postegresql-windows-e-linux/)
3. []()
4. []()
5. []()
6. []()
7. []()
8. []()
9. []()
10.[]()
