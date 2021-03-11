import unittest
from src import create_app


class CommonUnitTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test')
        self.app = self.app.test_client()
