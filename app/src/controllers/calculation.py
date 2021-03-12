# -- coding: utf-8 --
from flask import request
from flask_restx import Resource
from ..dtos import CalculationDto
from ..services import (
    create_calc,
    update_calc,
    delete_calc,
    select_calc,
    select_calcs
)

ns = CalculationDto.ns
_data_calculation = CalculationDto.data_calculation
_input_calculation = CalculationDto.input_calculation
_parser_calculation_id = CalculationDto.parser_calculation_id



@ns.route("")
@ns.doc(
    responses={
        200: 'OK',
        201: 'Created',
        500: 'InternelServerError'
    })
class Calc(Resource):
    @ns.marshal_list_with(_data_calculation, envelope='data', code=200, description='OK')
    def get(self):
        """ Get calculation list data

        Returns:
            Tuple[Dict[str, List[Calculation]], int]: dict: calculation 데이터, int: 통신 코드
        """
        
        return select_calcs()


    @ns.expect(_input_calculation, validate=True)
    @ns.marshal_with(_data_calculation, code=201, description='Created')
    def post(self):
        """ Create calculation data

        Returns:
            Tuple[Calculation, int]: dict: calculation 데이터, int: 통신 코드
        """
        
        data = request.json
        return create_calc(data)


@ns.route("/<int:calc_id>")
@ns.doc(
    responses={
        200: 'OK',
        404: 'CalcNotFound',
        500: 'InternelServerError'
    },
    parser=_parser_calculation_id)
class CalcId(Resource):
    @ns.marshal_with(_data_calculation, code=200, description='OK')
    def get(self, calc_id):
        """ Get calculation data by calc_id

        Returns:
            Tuple[Calculation, int]: dict: calculation 데이터, int: 통신 코드
        """
        
        return select_calc(calc_id=calc_id)

    @ns.expect(_input_calculation, validate=True)
    @ns.marshal_with(_data_calculation, code=200, description='OK')
    def put(self, calc_id):
        """ Update calculation data by calc_id

        Returns:
            Tuple[Calculation, int]: dict: calculation 데이터, int: 통신 코드
        """
        
        data = request.json
        return update_calc(calc_id=calc_id, data=data)

    @ns.marshal_with(_data_calculation, code=200, description='OK')
    def delete(self, calc_id):
        """ Delete calculation data by calc_id

        Returns:
            Tuple[Calculation, int]: dict: calculation 데이터, int: 통신 코드
        """
        
        return delete_calc(calc_id=calc_id)
