from flask_restx import abort
from sqlalchemy.orm.exc import NoResultFound
from typing import Dict, Union, List, NamedTuple
from datetime import datetime

from src import db
from src.models import (
    Calculation, CalculationSchema
)

calc_schema = CalculationSchema()
calcs_schema = CalculationSchema(many=True)

class CalculationResult(NamedTuple):
    data: Calculation
    status_code: int

class CalculationListResult(NamedTuple):
    data: List[Calculation]
    status_code: int


def create_calc(data: Dict[str, Union[str, int]]) -> CalculationResult:
    """ create calc data

    Args:
        data (dict): calc data

    Raises:
        InternelServerError: 서버 로직 오류

    Returns:
        CalculationResult: Calculation, status_code
    """
    try:
        result = eval("%s%s%s" % (data['num1'], data['symbol'], data['num2']))
        new_calc = Calculation(
            num1=data['num1'],
            num2=data['num2'],
            symbol=data['symbol'],
            result=result
        )
        db.session.add(new_calc)
        db.session.commit()

        return CalculationResult(data=calc_schema.dump(new_calc), status_code=201)

    except Exception as e:
        abort(500, message='InternelServerError')


def select_calcs() -> CalculationListResult:
    """ select all calc data

    Raises:
        InternelServerError: Internel server error

    Returns:
        CalculationListResult: List[Calculation], status_code
    """    
    try:
        calcs = Calculation.query.all()
        return CalculationListResult(data=calcs_schema.dump(calcs), status_code=200)

    except Exception as e:
        abort(500, message='InternelServerError')


def select_calc(calc_id: int) -> CalculationResult:
    """ select calc data by calc_id

    Args:
        calc_id (int): calc id

    Raises:
        CalcNotFound: Not found data
        InternelServerError: Internel server error

    Returns:
        CalculationResult: Calculation, status_code
    """
    try:

        calc = Calculation.query.get(calc_id)
        if not calc:
            raise NoResultFound('CalcNotFound')

        return CalculationResult(data=calc_schema.dump(calc), status_code=200)

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


def update_calc(calc_id: int, data: Dict[str, Union[str, int]]) -> CalculationResult:
    """ update calc data by calc_id

    Args:
        calc_id (int): calc id
        data (dict): calc data for update

    Raises:
        CalcNotFound: Not found data
        InternelServerError: Internel server error

    Returns:
        CalculationResult: Calculation, status_code
    """
    try:
        calc = Calculation.query.filter_by(calc_id=calc_id)
        
        if not calc.first():
            raise NoResultFound('CalcNotFound')
        else:
            result = eval("%s%s%s" % (data['num1'], data['symbol'], data['num2']))
            now_time = datetime.strptime(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
            update_data = dict(
                num1=data['num1'],
                num2=data['num2'],
                symbol=data['symbol'],
                result=result,
                update_date=now_time
            )

            calc.update(update_data, synchronize_session=False)
            db.session.commit()

        return CalculationResult(data=calc_schema.dump(calc.first()), status_code=200)

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


def delete_calc(calc_id: int) -> CalculationResult:
    """ delete calc data by calc_id

    Args:
        calc_id (int): calc id

    Raises:
        CalcNotFound: Not found data
        InternelServerError: Internel server error

    Returns:
        CalculationResult: Calculation, status_code
    """
    try:
        calc = Calculation.query.filter_by(calc_id=calc_id)
        
        if not calc.first():
            raise NoResultFound('CalcNotFound')
        else:
            now_time = datetime.strptime(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
            delete_data = dict(
                delete_date=now_time
            )

            calc.update(delete_data, synchronize_session=False)
            db.session.commit()

        return CalculationResult(data=calc_schema.dump(calc.first()), status_code=200)

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


