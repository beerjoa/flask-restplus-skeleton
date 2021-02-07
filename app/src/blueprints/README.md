# API versioning


## Usage

v1013.py

```python
# -- coding: utf-8 --

from flask import Blueprint
from flask_restplus import Api

## import namespaces made in 'apis/v1013' directory.
from ..apis.v1013.calc import ns as calc
from ..apis.v1013.result import ns as result


authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

## build a blueprint for versioning with url_prefix you want.
blueprint = Blueprint('api_1013', __name__, url_prefix='/v1013')

api: Api = Api(blueprint, version='1.0.13', title='Basic API v1.0.13',
               description='basic rest api', doc='/swagger',
               security='Bearer Auth', authorizations=authorizations)

## add namespace imported above to the blueprint
api.add_namespace(calc)
api.add_namespace(result)


```