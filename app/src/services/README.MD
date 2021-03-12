# Service


## Usage

[calculation.py](https://github.com/beerjoa/flask-restplus-skeleton/tree/master/app/src/blueprints/v1.py)

```python
# -- coding: utf-8 --
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
    """ create func

    Args:
        ...

    Raises:
        ...

    Returns:
        ...
    """
    try:

        ...
        
        return CalculationResult(data=data, status_code=status_code)

    except Exception as e:
        abort(500, message='InternelServerError')


def select_calcs() -> CalculationListResult:
    """ select list func

    Args:
        ...

    Raises:
        ...

    Returns:
        ...
    """
    try:
        
        ...

        return CalculationListResult(data=data, status_code=status_code)

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


def select_calc(calc_id: int) -> CalculationResult:
    """ select func

    Args:
        ...

    Raises:
        ...

    Returns:
        ...
    """
    try:

        ...

        return CalculationResult(data=data, status_code=status_code)

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


def update_calc(calc_id: int, data: Dict[str, Union[str, int]]) -> CalculationResult:
    """ update func

    Args:
        ...

    Raises:
        ...

    Returns:
        ...
    """
    try:

        ...

        return CalculationResult(data=data, status_code=status_code)

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


def delete_calc(calc_id: int) -> CalculationResult:
    """ delete func

    Args:
        ...

    Raises:
        ...

    Returns:
        ...
    """
    try:
        
        ...

        return CalculationResult(data=data, status_code=status_code)

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')



```