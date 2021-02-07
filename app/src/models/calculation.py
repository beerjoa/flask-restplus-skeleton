from src import db
import datetime

class Calculation(db.Model):
    __table_name__ = 'calculation'

    calc_id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(200), nullable=False)
    create_date = db.Column(db.DateTime(), default=datetime.datetime.utcnow, nullable=False)

    def __init__(self, result):
        self.result = result

    def __repr__(self):
        return f"<Calculation('{self.calc_id}', '{self.result}', '{self.create_date}')>"