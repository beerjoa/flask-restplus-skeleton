# flask-restplus-skeleton

[![Build Status](https://travis-ci.com/beerjoa/flask-restplus-skeleton.svg?branch=master)](https://travis-ci.com/beerjoa/flask-restplus-skeleton)
[![Coverage Status](https://coveralls.io/repos/github/beerjoa/flask-restplus-skeleton/badge.svg?branch=master)](https://coveralls.io/github/beerjoa/flask-restplus-skeleton?branch=master)

*Make sure you have `pyenv` and `pyenv-virtualenv` installed beforehand*

## Features
- [Flask-Restx](https://flask-restx.readthedocs.io/en/latest/) > framework for quickly building REST APIs
- [pytest](https://docs.pytest.org/en/stable/contents.html) > Unit testing 
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/) > JWT Authentication
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) > Database ORM
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) > Database Migrations
- Swagger Documentation 
- API versioning via Blueprints -> [link](https://github.com/beerjoa/flask-restplus-skeleton/tree/master/app/src/blueprints)
- Layered Architecture 
    > [controller](https://github.com/beerjoa/flask-restplus-skeleton/tree/master/app/src/controllers)

    > [service](https://github.com/beerjoa/flask-restplus-skeleton/tree/master/app/src/services/README.MD)

    > [dto](https://github.com/beerjoa/flask-restplus-skeleton/tree/master/app/src/dtos), [model](https://github.com/beerjoa/flask-restplus-skeleton/tree/master/app/src/models)

## Requirements
- pyenv
- pyenv-virtualenv

## Usage


### Install

#### 1. Install the virtual environment


```bash
### Install pyenv and pyenv-virtualenv on Linux or MacOS
$ make install-pyenv
```

```bash
### Install python v3.7.4 using pyenv
$ pyenv install 3.7.4
```

#### 2. Build the virtual environment and install requirements

```bash
$ make build
```

#### 3. Database migrations

```bash
### run commands in '/app'
### create a migration repository 
$ cd app 
$ flask db init

### generate a migration
$ flask db migrate -m "first migration."

### apply the migration to the database
$ flask db upgrade
```

### Run
Specify flask app environment variables in a [`.flaskenv`](https://github.com/beerjoa/flask-restplus-skeleton/blob/master/app/.flaskenv) file

```bash
### run commands in '/app'
$ flask run

### Swagger Documentation -> http://host:port/swagger
```


### Test

```bash
$ pytest app/tests
```


## Reference

- [status code WIKI](https://ko.wikipedia.org/wiki/HTTP_%EC%83%81%ED%83%9C_%EC%BD%94%EB%93%9C#3xx_(%EB%A6%AC%EB%8B%A4%EC%9D%B4%EB%A0%89%EC%85%98_%EC%99%84%EB%A3%8C))
- [Makefile for a Python environment with pyenv-virtualenv](https://gist.github.com/genyrosk/2a6e893ee72fa2737a6df243f6520a6d)
- [Flask Command Line Interface](https://flask.palletsprojects.com/en/1.1.x/cli/)