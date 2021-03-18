from flask_restx import abort
from sqlalchemy.orm.exc import NoResultFound
from typing import Dict, Union, List, NamedTuple

from ..models import (
    Calculation, CalculationSchema
)

_calculation = Calculation()
_calc_schema = CalculationSchema()
_calc_list_schema = CalculationSchema(many=True)

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
        InternelServerError: Internel server error

    Returns:
        CalculationResult: Calculation, status_code
    """
    try:
        new_calc = _calculation.create(data=data)
        return CalculationResult(data=_calc_schema.dump(new_calc), status_code=201)

    except Exception as e:
        abort(500, message='InternelServerError')


def select_calc_list() -> CalculationListResult:
    """ select all calc data

    Raises:
        InternelServerError: Internel server error

    Returns:
        CalculationListResult: List[Calculation], status_code
    """    
    try:
        calcs = _calculation.select_all()
        return CalculationListResult(data=_calc_list_schema.dump(calcs), status_code=200)

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
        calc = _calculation.select_id(calc_id=calc_id)
        if not calc.first():
            raise NoResultFound('CalcNotFound')

        return CalculationResult(data=_calc_schema.dump(calc.first()), status_code=200)

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
        calc = _calculation.select_id(calc_id=calc_id)
        
        if not calc.first():
            raise NoResultFound('CalcNotFound')
        else:
            calc = _calculation.update(calc=calc, data=data)

        return CalculationResult(data=_calc_schema.dump(calc.first()), status_code=200)

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
        calc = _calculation.select_id(calc_id=calc_id)
        
        if not calc.first():
            raise NoResultFound('CalcNotFound')
        else:
            calc = _calculation.delete(calc=calc)

        return CalculationResult(data=_calc_schema.dump(calc.first()), status_code=200)

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


