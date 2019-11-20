from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.maximize_window()

driver.implicitly_wait(30)

url = r"file:///Users/annie/Desktop/test_page/registerA.html"
driver.get(url)


sleep(2)
js = "window.scrollTo(0, 10000)"
driver.execute_script(js)


sleep(2)

driver.quit()