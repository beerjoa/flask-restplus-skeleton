from .util.common import CommonUnitTest
from src.models.calculation import (
    Calculation,
    CalculationSchema
)
from src.dtos import CalculationDto as ns_calc
import json



class PostCalcUnitTest(CommonUnitTest):
    def runTest(self):
        input_calculation = dict(
            num1= 1,
            num2= 2,
            symbol="+"
        )
        response = self.app.post('/v1/calculations', json=input_calculation)
        data = json.loads(response.get_data())
        self.assertEqual(201, response.status_code)
        self.assertEqual(type({}), type(data))


class GetCalcsUnitTest(CommonUnitTest):
    def runTest(self):
        response = self.app.get('/v1/calculations')
        data = json.loads(response.get_data())
        self.assertEqual(200, response.status_code)
        self.assertEqual(type({}), type(data))

class GetCalcByCaclIdUnitTest(CommonUnitTest):
    def runTest(self):
        calc_id = 1
        response = self.app.get(f'/v1/calculations/{calc_id}')
        data = json.loads(response.get_data())
        self.assertEqual(200, response.status_code)
        self.assertEqual(type({}), type(data))


class PutCalcUnitTest(CommonUnitTest):
    def runTest(self):
        calc_id = 1
        input_calculation = dict(
            num1= 2,
            num2= 2,
            symbol="+"
        )
        response = self.app.put(f'/v1/calculations/{calc_id}', json=input_calculation)
        data = json.loads(response.get_data())
        self.assertEqual(200, response.status_code)
        self.assertEqual(type({}), type(data))


class DeleteCalcUnitTest(CommonUnitTest):
    def runTest(self):
        calc_id = 1
        response = self.app.delete(f'/v1/calculations/{calc_id}')
        data = json.loads(response.get_data())
        self.assertEqual(200, response.status_code)
        self.assertEqual(type({}), type(data))

