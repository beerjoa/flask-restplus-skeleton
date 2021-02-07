import unittest
from src import create_app
import json


class CommonUnitTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app = self.app.test_client()


class ResultListUnitTestSuccess(CommonUnitTest):
    def runTest(self):
        response = self.app.get('/result')
        data = json.loads(response.get_data())
        self.assertEqual(type([]), type(data))


class ResultByIdUnitTestSuccess(CommonUnitTest):
    def runTest(self):
        response = self.app.get('/result/1')
        data = json.loads(response.get_data())
        self.assertEqual(type({}), type(data))

