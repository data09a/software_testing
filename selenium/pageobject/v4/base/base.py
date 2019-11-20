from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # initial
    def __init__(self):

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://localhost")

    # find elements
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # click
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # input method
    def base_input(self, loc, value):
        el = self.base_find_element(loc)

        el.clear()

        el.send_keys(value)

    # get text
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # get screen shot
    def base_get_image(self):
        self.driver.get_screenshot_as_file("./image/fail.png")
