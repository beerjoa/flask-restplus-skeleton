# -- coding: utf-8 --

from flask import Blueprint
from flask_restplus import Api
from ..apis.root.calc import ns as calc


authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

blueprint = Blueprint('api', __name__)

api: Api = Api(blueprint, version='1.0', title='Basic API',
               description='basic rest api', doc='/swagger',
               security='Bearer Auth', authorizations=authorizations)

api.add_namespace(calc)
