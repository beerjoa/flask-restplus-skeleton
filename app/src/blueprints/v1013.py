# -- coding: utf-8 --

from flask import Blueprint
from flask_restplus import Api
from ..apis.root.calc import ns as calc
from ..apis.root.result import ns as result


authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

blueprint = Blueprint('api_1013', __name__, url_prefix='/v1013')

api: Api = Api(blueprint, version='1.0.13', title='Basic API v1.0.13',
               description='basic rest api', doc='/swagger',
               security='Bearer Auth', authorizations=authorizations)

api.add_namespace(calc)
api.add_namespace(result)
