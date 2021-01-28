# -- coding: utf-8 --
import time
import logging
from flask import request
from flask_restplus import Namespace, fields, Resource, reqparse


logger = logging.getLogger('gunicorn.error')

ns = Namespace('calc', 'Calc api')

model_number = ns.model('numbers', {
    'num1': fields.Integer(readOnly=True, required=True, description='first number'),
    'num2': fields.Integer(readOnly=True, required=True, description='second number'),
    'symbol': fields.String(readOnly=True, required=True, description='symbol')
})

calc_parser = reqparse.RequestParser(bundle_errors=True)
calc_parser.add_argument('num1', default='1', required=True,
                         help='first number', type=int, location='args')
calc_parser.add_argument('num2', default='2', required=True,
                         help='second number', type=int, location='args')
calc_parser.add_argument('symbol', default='+', required=True,
                         help='symbol', type=str, location='args')


@ns.route("")
@ns.doc(responses={200: 'success', 300: 'Redirected', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
class calc(Resource):
    @ns.doc(parser=calc_parser)
    def get(self):
        """
        get method
        :return:
        """
        try:
            args = calc_parser.parse_args()
            logger.info(f"args :::: {args}")

            check_args = _check_args_invalid(
                args=args, keys=['num1', 'num2', 'symbol'])
            if not check_args:
                raise Exception('Invalid args')

            num1 = args['num1']
            num2 = args['num2']
            symbol = args['symbol']

            success, func_result = _func(num1, num2, symbol)

            if not success:
                raise Exception('failed processing')

            status = 'success'
            result = {'num': func_result}
            return {
                'status': status,
                'data': result
            }

        except Exception as e:
            ns.abort(400, message=e.__doc__, status='fail',
                     custom_msg=str(e),
                     errorCode='e201')

    @ns.expect(model_number)
    def post(self):
        """
        post method
        :return:
        """
        try:
            args = request.json
            logger.info(f"args :::: {args}")

            check_args = _check_args_invalid(args)
            if not check_args:
                raise Exception('Invalid args')

            num1 = args['num1']
            num2 = args['num2']
            symbol = args['symbol']

            success, func_result = _func(num1, num2, symbol)
            if not success:
                raise Exception('failed processing')

            status = 'success'
            result = {'num': func_result}

            return {
                'status': status,
                'data': result
            }

        except Exception as e:
            ns.abort(400, message=e.__doc__, status='fail',
                     custom_msg=str(e),
                     errorCode='e201')

    @ns.expect(model_number)
    def delete(self):
        """
        delete method
        :return:
        """
        try:
            args = request.json
            logger.info(f"args :::: {args}")

            check_args = _check_args_invalid(args)
            if not check_args:
                raise Exception('Invalid args')

            num1 = args['num1']
            num2 = args['num2']
            symbol = args['symbol']

            success, func_result = _func(num1, num2, symbol)

            if not success:
                raise Exception('failed processing')

            status = 'success'
            result = {'num': func_result}
            return {
                'status': status,
                'data': result
            }

        except Exception as e:
            ns.abort(400, message=e.__doc__, status='fail',
                     custom_msg=str(e),
                     errorCode='e201')

    @ns.expect(model_number)
    def put(self):
        """
        put method
        :return:
        """
        try:
            args = request.json
            logger.info(f"args :::: {args}")

            check_args = _check_args_invalid(args)
            if not check_args:
                raise Exception('Invalid args')

            num1 = args['num1']
            num2 = args['num2']
            symbol = args['symbol']

            success, func_result = _func(num1, num2, symbol)

            if not success:
                raise Exception('failed processing')

            status = 'success'
            result = {'num': func_result}
            return {
                'status': status,
                'data': result
            }

        except Exception as e:
            ns.abort(400, message=e.__doc__, status='fail',
                     custom_msg=str(e),
                     errorCode='e201')


def _func(num1, num2, symbol):
    try:
        flag = True
        result = eval(f"{num1}{symbol}{num2}")
    except:
        flag = False
        result = None
    finally:
        return flag, result


def _check_args_invalid(args, keys):
    try:
        for key, value in args.items():
            if value == None or key not in keys:
                raise Exception('')
        flag = True
    except:
        flag = False
    finally:
        return flag
