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

blueprint = Blueprint('api', __name__, url_prefix='/v1')

api: Api = Api(blueprint,
               version='1.0',
               title='Calculation API',
               description='Calculation api',
               doc='/swagger',
               security='Bearer Auth',
               authorizations=authorizations)

api.add_namespace(calc_ns)
