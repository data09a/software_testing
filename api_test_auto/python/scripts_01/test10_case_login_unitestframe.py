"""
    Goal：login in unitest frame

    Case data：
        1.verification code：http://192.168.176.128/index.php?m=Home&c=User&a=verify
        2.login：http://192.168.176.128/index.php?m=Home&c=User&a=do_login
            data = {"username": "ab123",
                    "password": "12345678",
                    "verify_code": 8888}

"""

# import unittest requests
import unittest
import requests


# create unittest.TestCase
class TPShopLogin(unittest.TestCase):
        # setUp
        def setUp(self):
                pass

        # tearDown
        def tearDown(self):
                pass

        # login successfully
        def test_login_success(self):
                pass

        # username not exist
        def test_username_not_exist(self):
                pass

        # password error
        def test_password_error(self):
                pass
