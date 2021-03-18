from .. import db
from .base import Base, BaseSchema
from typing import Dict, Union
from datetime import datetime

class Calculation(Base):
    __table_name__ = 'calculation'

    calc_id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Integer, nullable=False)
    num2 = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(20), nullable=False)
    result = db.Column(db.String(1000), nullable=False)

    def select_all(self):
        return Calculation.query.all()

    def select_id(self, calc_id: int):
        calc = Calculation.query.filter_by(calc_id=calc_id)
        return calc

    def create(self, data: Dict[str, Union[str, int]]):
        result = eval("%s%s%s" % (data['num1'], data['symbol'], data['num2']))
        new_calc = Calculation(
            num1=data['num1'],
            num2=data['num2'],
            symbol=data['symbol'],
            result=result
        )
        db.session.add(new_calc)
        db.session.commit()
        return new_calc
    
    def update(self, calc, data: Dict[str, Union[str, int]]):
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

        return calc

    def delete(self, calc):
        now_time = datetime.strptime(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        delete_data = dict(
            delete_date=now_time
        )

        calc.update(delete_data, synchronize_session=False)
        db.session.commit()

        return calc


class CalculationSchema(BaseSchema):
    class Meta:
        model = Calculation
        fields = (
            'calc_id', 
            'num1',
            'num2',
            'symbol', 
            'result', 
            'update_date',
            'delete_date',
            'create_date'
        )
        ordered = True