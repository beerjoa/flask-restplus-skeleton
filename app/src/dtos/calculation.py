# -- coding: utf-8 --
from flask_restx import Namespace, fields, reqparse

class CalculationDto:
    ns = Namespace('calculations', 'calculation namespace')

    ## model
    data_calculation = ns.model('data_calculation', {
        'calc_id': fields.Integer(readOnly=True, required=True, description='first number'),
        'num1': fields.Integer(readOnly=True, required=True, description='first number'),
        'num2': fields.Integer(readOnly=True, required=True, description='second number'),
        'symbol': fields.String(readOnly=True, required=True, description='symbol'),
        'result': fields.String(readOnly=True, required=True, description='result'),
        'update_date': fields.DateTime(required=False, description='updated date'),
        'delete_date': fields.DateTime(required=False, description='deleted date'),
        'create_date': fields.DateTime(required=False, description='created date')
    })

    ## input
    input_calculation = ns.model('input_calculation', {
        'num1': fields.Integer(readOnly=True, required=True, description='first number'),
        'num2': fields.Integer(readOnly=True, required=True, description='second number'),
        'symbol': fields.String(readOnly=True, required=True, description='symbol'),
    })

    ## parser
    parser_calculation_id = ns.parser()
    parser_calculation_id.add_argument('calc_id',help='calculation id', required=True, type=int, location='args')