Sistema Escolar
=======

Sistema de apresentação desenvolvido com Django 1.7
Banco de dados: SQLite

Antes de instalar este projeto, verifique os seguintes itens:
  - Instalação do Python;
  - Instalação do Django 1.7

Instalação
=========

Para instalar este projeto, clone o repositório GIT com o seguinte comando:
````sh
git clone https://github.com/dyegonery/escolar.git
````
Ou baixe o zip deste projeto em um diretório local com permissões de leitura e escrita.

Rodando o projeto
=========

Para executar a aplicação, navegue até a pasta do mesmo. Por exemplo: c:/python/escolar
Execute os seguintes comandos no terminal, ou prompt de comando do WIndows.
````sh
python manage.py makemigrations
python manage.py migrate
````
Os comandos acima criam as tabelas do banco de dados necessario para o site funcionar.
Após isso, você deverá executar o servidor web para executar a aplicação:
````sh
python manage.py runserver
````

Acessando o endereço 127.0.0.1:8000 você acessará a página inicial da aplicação.

Funcionamento
===========

O sistema possui três tabelas
  - Alunos
  - Turmas
  - Provas

Seguindo os requisitos do projeto, os seguintes campos obrigatórios estão presentes
  - DateField: Prova.data
  - CharField: Aluno.nome
  - ForeignKey: Aluno.turma
  - ManyToManyField: Aluno.provas
  - DecimalField: Prova.valor

Para desenvolvimento do mesmo, também foi utilizado o Twitter Bootstrap 3.


