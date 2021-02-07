import unittest
from src import create_app
import json

class CommonUnitTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app = self.app.test_client()


class CalcUnitTestSuccess(CommonUnitTest):
    def runTest(self):
        data = {
            'num1': 1,
            'num2': 1,
            'symbol': "+"
        }
        response = self.app.delete('/calc', json=data)
        data = json.loads(response.get_data())
        self.assertEqual('success', data["status"])
        self.assertEqual(type({}), type(data['data']))


class CalcUnitTestFail(CommonUnitTest):
    def runTest(self):
        data = {
            'num1': 1,
            'num2': 1,
            'symbol': None
        }
        response = self.app.delete('/calc', json=data)
        data = json.loads(response.get_data())
        self.assertEqual('fail', data["status"])
        self.assertEqual(type({}), type(data['data']))
