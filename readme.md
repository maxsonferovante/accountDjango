# Account Management System - Django

## Description

Este projeto é uma aplicação em Django com banco de dados SQLite, que permite a criação, listagem e login de usuários.

## Uso
1. Clone o repositório Git::

```shell
  git clone https://github.com/maxsonferovante/accountDjango

```
2. Crie um Ambiente Virtual e instale as dependências (Instruções para Linux. Veja a documentação do [Python](https://docs.python.org/pt-br/3/library/venv.html) para outras plataformas).
```shell
  cd project_directory
```
```shell
  python3 -m venv venv
```
```shell
  source venv/bin/activate   
```  
```shell
  pip3 install -r requirements.txt
```

3. Execute as Migrações

```shell
  python manage.py makemigrations
  python manage.py migrate
```

4. Execute a Aplicação:
```shell
  python manage.py runserver
```

4. Acesse a aplicação no navegador:
> http://localhost:8000 


## Ferramentas Utilizadas

- Python 3.11
- Django 5.0.7
- Django-htmx 
- SQLite

## Autor

- [Maxson Almeida](https://www.linkedin.com/in/maxson-almeida/)