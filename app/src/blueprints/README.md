# API versioning


## Usage

[v1.py](https://github.com/beerjoa/flask-restplus-skeleton/tree/master/app/src/blueprints/v1.py)

```python

# -- coding: utf-8 --

from flask import Blueprint
from flask_restx import Api
from ..controllers import (calc_ns)
authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

## build a blueprint for versioning with url_prefix you want.
blueprint = Blueprint('api', __name__, url_prefix='/v1')

api: Api = Api(blueprint,
               version='1.0',
               title='Calculation API',
               description='Calculation api',
               doc='/swagger',
               security='Bearer Auth',
               authorizations=authorizations)

## add namespace imported above to the blueprint
api.add_namespace(calc_ns)


```