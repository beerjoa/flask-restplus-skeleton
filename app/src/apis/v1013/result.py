# -- coding: utf-8 --
import time
import logging
from flask import request
from flask_restplus import Namespace, fields, Resource, reqparse
from src.models import Calculation

ns = Namespace('result', 'Calculation result api')

model_calc_result = ns.model('result', {
    'calc_id': fields.Integer,
    'result': fields.String,
    'create_date': fields.DateTime
})

@ns.route("")
@ns.doc(responses={200: 'success', 300: 'Redirected', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
class ResultList(Resource):
    @ns.marshal_with(model_calc_result)
    def get(self):
        """
        get result list
        :return:
        """
        return Calculation.query.all()


@ns.route("/<int:calc_id>")
@ns.doc(responses={200: 'success', 300: 'Redirected', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
class ResultById(Resource):
    @ns.marshal_with(model_calc_result)
    def get(self, calc_id):
        """
        get result by calc_id
        :return:
        """
        return Calculation.query.get(calc_id)

