## Virtual Environment
`python3 -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

## Pre-commit
`git commit -m "Some comments" --no-verify`

## Django
`python manage.py showmigrations`

`python manage.py migrate <app_name> <migration_number>`

`python manage.py migrate --fake`
## Run Project

`source tools/run_development.sh`

`source tools/exec_bash.sh`

## Docker
`docker build --tag <project_name> .` - build and name the image

`docker run --publish 8000:8000 <project_name>` - run the image by the name

`docker-compose build` - build from the `yml` file

`docker-compose run --rm sole django-admin startapp <app_name>`

`docker-compose up`

`docker kill $(docker ps -q)`

`sudo apachectl stop`

## Postgresql
`psql -d <db_name> - enter postgresql command line

`\dt`-show tables

`create database <db_name>;` - CREATE DATABASE

`create user <username> superuser;` - CREATE ROLE

`alter user <username> with password '<password>';` - ALTER ROLE



Part#1
docker build --tag python-django .
docker run --publish 8000:8000 python-django
Part#2
docker-compose build
docker-compose run --rm app django-admin startproject core .
docker-compose up
Part#3
docker-compose build
docker-compose run --rm app django-admin startproject core .
docker-compose up
docker exec -it django_container /bin/bash


Part#1
docker build --tag python-django .
docker run --publish 8000:8000 python-django
Part#2
docker-compose build
docker-compose run --rm app django-admin startproject core .
docker-compose up
Part#3
docker-compose build
docker-compose run --rm app django-admin startproject core .
docker-compose up
docker exec -it django_container /bin/bash
Part#4
docker-compose run django_app sh -c "django-admin startapp newapp ."
docker exec -it django_app sh

#Run Celery Task
    python manage.py shell
    from newapp.tasks import add
    add.delay(2, 2)

Info:
PYTHONUNBUFFERED:
Setting the non-empty value of PYTHONUNBUFFERED means
that the python output is transmitted directly to the
terminal without being buffered and that allows displaying
the application???s output in real-time.



