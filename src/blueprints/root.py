# -- coding: utf-8 --

import configparser
from apis.root.calc import ns as calc
from flask_restplus import Api
from flask import Blueprint
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
