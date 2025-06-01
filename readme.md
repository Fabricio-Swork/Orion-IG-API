API Rest Framawork.md
# INSTALL 

Ambiente virtual
> python -m venv venv 
> .\venv\Scripts\Activate.ps1

Django 
> python -m pip install django djangorestframework
> django-admin startproject core .
> django-admin startapp api

Teatar servidor 
> py manage.py runserver
obs: encerrar servidor logo apos para finalizar instalaçao

Criar Banco e tabelas ( sqlite)
> py manage.py migrate

Criar super user
> py manage.py createsuperuser

## Crie uma segunda conexão de banco de dados só para consulta

``` python

 'readonly': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'consulta_db',
        'USER': 'readonly_user',
        'PASSWORD': 'readonly_pass',
        'HOST': 'localhost',
        'PORT': '5432',
    },
``` 


# UVICORN

## COMANDO PARA RODAR EM PRODUÇÃO
> uvicorn core.asgi:application --host 127.0.0.1 --port 8000 --lifespan off

# NGINX

## Testar se esta escutando 

> netstat -an | findstr :80  

Obs: procurar na linha de registro: 
TCP     0.0.0.0:80      LISTENING

## Reiniciar Nginx

``` bash
    cd C:\nginx
nginx -s reload
```

## Para e iniciar Nginx
``` bash
    cd C:\nginx
    nginx -s stop
    nginx
```

# COLLECTSTATIC
Comando para centralizar todos os arquivo staticos na pasta

> python manage.py collectstatic

