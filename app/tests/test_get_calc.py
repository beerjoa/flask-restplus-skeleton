import unittest
from src import create_app
import json


class CommonUnitTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app = self.app.test_client()


class CalcUnitTestSuccess(CommonUnitTest):
    def runTest(self):
        params = {
            'num1': 1,
            'num2': 1,
            'symbol': "+"
        }
        response = self.app.get('/calc', query_string=params)
        data = json.loads(response.get_data())
        self.assertEqual('success', data["status"])
        self.assertEqual(type({}), type(data['data']))


class CalcUnitTestFail(CommonUnitTest):
    def runTest(self):
        params = {
            'num1': 1,
            'num2': 1,
            'symbol': "string"
        }
        response = self.app.get('/calc', query_string=params)
        data = json.loads(response.get_data())
        self.assertEqual('fail', data["status"])
        self.assertEqual(type({}), type(data['data']))
