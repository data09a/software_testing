import unittest
from parameterized import parameterized

class TestPara(unittest.TestCase):
    @parameterized.expand([("admin", "123456"), ("user002", "654321")])
    def test_para(self, username, password):
        print("username:", username)
        print("password:", password)