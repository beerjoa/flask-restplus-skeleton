from flask_restx import abort
from sqlalchemy import and_, or_, not_
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from typing import Dict, Tuple, Union
from datetime import datetime

from src import db
from src.models import (
    Calculation, CalculationSchema
)

calc_schema = CalculationSchema()
calcs_schema = CalculationSchema(many=True)


def create_calc(data: Dict[str, Union[str, int]]):# -> Tuple[Calculation, int]:
    """새로운 tag 추가 함수

    Args:
        data (dict): 추가하려는 calculation 데이터

    Raises:
        InternelServerError: 서버 로직 오류

    Returns:
        Tuple[Calculation, int]: dict: tag 데이터, int: 통신 코드
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

        return calc_schema.dump(new_calc), 201

    except Exception as e:
        abort(500, message='InternelServerError')


def select_calcs():# -> Tuple[Calculation, int]:

    try:
        calcs = Calculation.query.all()
        return calcs_schema.dump(calcs), 200

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


def select_calc(calc_id: int):# -> Tuple[Calculation, int]:

    try:

        calc = Calculation.query.get(calc_id)
        if not calc:
            raise NoResultFound('CalcNotFound')

        return calc_schema.dump(calc), 200

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


def update_calc(calc_id: int, data: Dict[str, Union[str, int]]):# -> Tuple[Calculation, int]:
    """ calc_id에 해당하는 calculation 수정 함수

    Args:
        calc_id (int): Calculation ID
        data (dict): 수정 calculation 데이터

    Raises:
        NoResultFound: calc_id에 해당하는 데이터가 존재하지 않을 때
        InternelServerError: 서버 로직 오류

    Returns:
        Tuple[Calculation, int]: dict: tag 데이터, int: 통신 코드
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

        return calc_schema.dump(calc.first()), 200

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


def delete_calc(calc_id: int):# -> Tuple[Calculation, int]:
    """ calc_id에 해당하는 calculation 삭제

    Args:
        calc_id (int): Calculation ID

    Raises:
        NoResultFound: calc_id에 해당하는 데이터가 존재하지 않을 때
        InternelServerError: 서버 로직 오류

    Returns:
        Tuple[Calculation, int]: dict: tag 데이터, int: 통신 코드
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

        return calc_schema.dump(calc.first()), 200

    except NoResultFound as e:
        abort(404, message=str(e))
    except Exception as e:
        abort(500, message='InternelServerError')


