# CNAB DOCS

Aplicação back-end feita para receber um arquivo CNBA.txt armazenar os dados em um banco de dados SQlite3 e retornar em tela pela propria aplicação.

## Linguagem e Tecnologias utilizadas no Projeto

- Python
- Django Framework
- SQlite3
- Django Rest Framework
- ORM do Django
- HTML
- CSS

## Instalação

**-Faça o clone do repositório pelo link SSH:**

`git clone git@github.com:agnes-lica/CNAB_DOCS.git`

- Ou acesse o repositório e crie um fork:

  `https://github.com/agnes-lica/CNAB_DOCS`

**-Ative o ambiente virtual no seu computador**

Na pasta do repositório clonado, digite os comandos:

`python -m venv venv`

E depois;

`source venv/bin/activate`

**-Instale os pacores do requirements.txt pelo comando:**

`pip install -r requirements.txt`

**-Crie o banco de dados SQlite3 no seu computador utilizando o comando**

`python manage.py migrate`

## Funcionamento

**Execute o comando abaixo para iniciar o servidor**

`python manage.py runserver`

Existem duas URL's disponíveis para acesso:

1. **http://127.0.0.1:8000/transactions/upload/** - para fazer upload do arquivo CNAB txt
2. **http://127.0.0.1:8000/transactions/transactions/** - para realizar a vizualização das informações.
