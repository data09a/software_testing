# import (unittest 、api tool、requests)
import unittest

import requests

from api_login import ApiLogin


# create new test class
class TestLogin(unittest.TestCase):
    login = ApiLogin()

    # setUp
    def setUp(self):
        self.session = requests.session()

    # tearDown
    def tearDown(self):
        self.session.close()

    # login successfully
    def test_login_success(self):
        self.login.api_get_verify(self.session)

        r = self.login.api_post_login(self.session, "ab123", "12345678", 8888)
        try:
            self.assertEqual(200, r.status_code)

            self.assertEqual("Login Successfully", r.json()['msg'])
        except AssertionError as e:
            print(e)

    # username does not exist
    def test_username_not_exist(self):

        self.login.api_get_verify(self.session)

        r = self.login.api_post_login(self.session, "ab123", "12345678", 8888)
        try:

            self.assertEqual(200, r.status_code)

            self.assertEqual("The account does not exist!", r.json()['msg'])
        except AssertionError as e:
            print(e)

    # password is incorrect
    def test_password_error(self):

        self.login.api_get_verify(self.session)

        r = self.login.api_post_login(self.session, "ab123", "12345678", 8888)
        try:

            self.assertEqual(200, r.status_code)

            self.assertEqual("The password is incorrect!", r.json()['msg'])
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
