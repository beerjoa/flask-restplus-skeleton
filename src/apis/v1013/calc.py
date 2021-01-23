# -- coding: utf-8 --
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Namespace, fields, Resource, reqparse
from flask import request
import logging
import time
from errors import error



logger = logging.getLogger('gunicorn.error')

custom_error = error.CustomError()

ns = Namespace('calc', 'Calc api')

model_number = ns.model('numbers', {
    'num1': fields.Integer(readOnly=True, required=True, description='첫번째 숫자', help='필수'),
    'num2': fields.Integer(readOnly=True, required=True, description='두번째 숫자', help='필수'),
    'symbol': fields.String(readOnly=True, required=True, description='연산기호', help='필수')
})

calc_parser = reqparse.RequestParser(bundle_errors=True)
calc_parser.add_argument('num1', default='1', required=True, help='첫번째 숫자', type=int, location='args')
calc_parser.add_argument('num2', default='2', required=True, help='두번째 숫자', type=int, location='args')
calc_parser.add_argument('symbol', default='+', required=True, help='연산기호', type=str, location='args')


@ns.route("")
@ns.doc(responses={200: 'get Success', 300: 'Redirected', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
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

            try:
                check_args = check_args_invalid(args)
                if not check_args:
                    raise Exception('Invalid args or request data') 

                num1 = args['num1']
                num2 = args['num2']
                symbol = args['symbol']


                success, func_result = func(num1, num2, symbol)

                if not success:
                    raise Exception('') 
                    
                status = 'success'
                result = {'num':func_result}
            except Exception as e:
                status = 'fail'
                result = custom_error.error_format(code='e201', custom_msg=str(e))

            finally:
                return {
                    'status': status,
                    'data': result
                }


        except KeyError as e:
            ns.abort(500, e.__doc__, status="Could not save information", statusCode="500")
        except Exception as e:
            ns.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @ns.expect(model_number)
    def post(self):
        """
        post method
        :return:
        """
        try:
            args = request.json
            logger.info(f"args :::: {args}")

            try:
                check_args = check_args_invalid(args)
                if not check_args:
                    raise Exception('Invalid args or request data') 

                num1 = args['num1']
                num2 = args['num2']
                symbol = args['symbol']

                success, func_result = func(num1, num2, symbol)

                if not success:
                    raise Exception('') 
                    
                status = 'success'
                result = {'num':func_result}
            except Exception as e:
                status = 'fail'
                result = custom_error.error_format(code='e201', custom_msg=str(e))

            finally:
                return {
                    'status': status,
                    'data': result
                }


        except KeyError as e:
            ns.abort(500, e.__doc__, status="Could not save information", statusCode="500")
        except Exception as e:
            ns.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @ns.expect(model_number)
    def delete(self):
        """
        delete method
        :return:
        """
        try:
            args = request.json
            logger.info(f"args :::: {args}")

            try:
                check_args = check_args_invalid(args)
                if not check_args:
                    raise Exception('Invalid args or request data') 

                num1 = args['num1']
                num2 = args['num2']
                symbol = args['symbol']

                success, func_result = func(num1, num2, symbol)

                if not success:
                    raise Exception('') 
                    
                status = 'success'
                result = {'num':func_result}
            except Exception as e:
                status = 'fail'
                result = custom_error.error_format(code='e201', custom_msg=str(e))

            finally:
                return {
                    'status': status,
                    'data': result
                }


        except KeyError as e:
            ns.abort(500, e.__doc__, status="Could not save information", statusCode="500")
        except Exception as e:
            ns.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")

    @ns.expect(model_number)
    def put(self):
        """
        put method
        :return:
        """
        try:
            args = request.json
            logger.info(f"args :::: {args}")

            try:
                check_args = check_args_invalid(args)
                if not check_args:
                    raise Exception('Invalid args or request data') 

                num1 = args['num1']
                num2 = args['num2']
                symbol = args['symbol']

                success, func_result = func(num1, num2, symbol)

                if not success:
                    raise Exception('') 
                    
                status = 'success'
                result = {'num':func_result}
            except Exception as e:
                status = 'fail'
                result = custom_error.error_format(code='e201', custom_msg=str(e))

            finally:
                return {
                    'status': status,
                    'data': result
                }


        except KeyError as e:
            ns.abort(500, e.__doc__, status="Could not save information", statusCode="500")
        except Exception as e:
            ns.abort(400, e.__doc__, status="Could not retrieve information", statusCode="400")


def func(num1, num2, symbol):
    try:
        flag = True
        result = eval(f"{num1}{symbol}{num2}")
    except:
        flag = False
        result = None
    return flag, result


def check_args_invalid(args):
    result = True
    if None in args.values():
        result = False
    # elif:

    return result

