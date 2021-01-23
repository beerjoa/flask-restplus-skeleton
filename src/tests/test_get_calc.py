import unittest
from app import app
import requests
import json
import io


class CommonUnitTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()


class CalcUnitTestSuccess(CommonUnitTest):
    def runTest(self):
        params = {
            'num1': 1,
            'num2': 1,
            'symbol': "+"
        }
        response = self.app.get('/calc',query_string=params)
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
        response = self.app.get('/calc',query_string=params)
        data = json.loads(response.get_data())
        self.assertEqual('fail', data["status"])
        self.assertEqual(type({}), type(data['data']))


if __name__ == '__main__':
    unittest.main()
