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

blueprint = Blueprint('api_1013', __name__, url_prefix='/v2')

api: Api = Api(blueprint,
               version='2.0',
               title='Calculation API v2',
               description='Calculation api',
               doc='/swagger',
               security='Bearer Auth',
               authorizations=authorizations)

api.add_namespace(calc_ns)