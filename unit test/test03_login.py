import unittest
import time
from time import sleep
from selenium import webdriver


class TestLogin(unittest.TestCase):


    def setUp(self):

        self.driver = webdriver.Firefox()

        self.driver.get("http://localhost")

        self.driver.maximize_window()

        self.driver.implicitly_wait(30)


    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def test_login_code_null(self):
        driver = self.driver

        driver.find_element_by_partial_link_text("Login").click()
        driver.find_element_by_css_selector("#username").send_keys("abc123")

        driver.find_element_by_css_selector("#password").send_keys("123456")

        driver.find_element_by_css_selector("#verify_code").send_keys("")

        driver.find_element_by_css_selector(".J-login-submit").click()
        result = driver.find_element_by_css_selector(".layui-layer-content").text
        print("result：", result)

        expect_result = "The verification code can not be empty ！！"
        try:
            self.assertEqual(result, expect_result)
        except AssertionError:
            driver.get_screenshot_as_file("image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

            raise