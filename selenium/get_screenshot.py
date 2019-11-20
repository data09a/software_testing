
from time import strftime
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.maximize_window()

driver.implicitly_wait(30)

url = r"file:///Users/annie/Desktop/test_page/registerA.html"
driver.get(url)



driver.find_element_by_css_selector("#userA").send_keys("admin")

driver.get_screenshot_as_file("image/%s.png"%(strftime("%Y_%m_%d %H_%M_%S")))


sleep(2)

driver.quit()