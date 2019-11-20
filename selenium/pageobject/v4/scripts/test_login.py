import unittest
from v4.page.page_login import PageLogin
from parameterized import parameterized


def get_data():
    return [("abc123", "123456", "8888", "account does not exist!"),
            ("cad123", "123123", "8888", "password is not correct!")]

# set up new test method and inherited
class TestLogin(unittest.TestCase):
    login = None
    # setUp

    @classmethod
    def setUpClass(cls):

        cls.login = PageLogin()

        cls.login.page_click_login_link()

    # tearDown
    @classmethod
    def tearDownClass(cls):

        cls.login.driver.quit()

    # login test
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, code, expect_result):

        self.login.page_login(username, pwd, code)

        msg = self.login.page_get_error_info()
        try:

            self.assertEqual(msg, expect_result)
        except AssertionError:

            self.login.page_get_img()
