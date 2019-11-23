"""
    Goal：login in unitest frame

    Case data：
        1.verification code：http://192.168.176.128/index.php?m=Home&c=User&a=verify
        2.login：http://192.168.176.128/index.php?m=Home&c=User&a=do_login
            data = {"username": "ab123",
                    "password": "12345678",
                    "verify_code": 8888}

"""

## import unittest requests
import unittest
import requests


## create unittest.TestCase
class TPShopLogin(unittest.TestCase):
        # setUp
        def setUp(self):
                # get session
                self.session = requests.session()
                # login url
                self.url_login = "http://192.168.176.128/index.php?m=Home&c=User&a=do_login"
                # verify code url
                self.url_verify = "http://192.168.176.128/index.php?m=Home&c=User&a=verify"

        # tearDown
        def tearDown(self):
                # close session
                self.session.close()

        # login successfully
        def test_login_success(self):
                # get verify code --> get cookies
                self.session.get(self.url_verify)
                # request to login
                data = {"username": "ab123",
                        "password": "12345678",
                        "verify_code": 8888}
                r = self.session.post(self.url_login, data=data)
                try:

                        self.assertEqual("Login Successfully", r.json()['msg'])
                except AssertionError as e:
                        print(e)

        # username does not exist
        def test_username_not_exist(self):
                self.session.get(self.url_verify)
                data = {"username": "ab123",
                        "password": "12345678",
                        "verify_code": 8888}
                r = self.session.post(self.url_login, data=data)
                try:

                        self.assertEqual("The account does not exist!", r.json()['msg'])
                except AssertionError as e:
                        print(e)

        # password is incorrect 
        def test_password_error(self):
                self.session.get(self.url_verify)

                data = {"username": "ab123",
                        "password": "12345678",
                        "verify_code": 8888}
                r = self.session.post(self.url_login, data=data)
                try:

                        self.assertEqual("The password is incorrect!", r.json()['msg'])
                except AssertionError as e:
                        print(e)


if __name__ == '__main__':
    unittest.main()