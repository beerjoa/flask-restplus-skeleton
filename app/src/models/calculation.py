import datetime
from src import db, ma

from sqlalchemy.sql import functions

class Calculation(db.Model):
    __table_name__ = 'calculation'

    calc_id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Integer, nullable=False)
    num2 = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(20), nullable=False)
    result = db.Column(db.String(1000), nullable=False)
    update_date = db.Column(db.DateTime(), nullable=True)
    delete_date = db.Column(db.DateTime(), nullable=True)
    create_date = db.Column(db.DateTime(), server_default=functions.current_timestamp(), nullable=False)



class CalculationSchema(ma.Schema):
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